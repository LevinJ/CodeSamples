#include <iostream>
#include <string>
#include <thread>
#include <mutex>
#include <condition_variable>
#include <chrono>
#include <atomic>

std::string data;


class ThreadUtil
{
private:
	bool m_paused;
	bool m_resume_onetime ;
	bool m_debug_mode;
	std::mutex m_m;
	std::condition_variable m_cv;
public:
	ThreadUtil(){
		m_paused = false;
		m_resume_onetime = false;
		m_debug_mode = false;
	}
	void pause_tracking(){
		m_debug_mode = true;
		//wait for paused confirmation from thread 2
		std::unique_lock<std::mutex> lk(m_m);
		m_cv.wait(lk, [this]{return m_paused;});
	}
	void track_next_frame(){
		{
			std::unique_lock<std::mutex> lk(m_m);
			m_resume_onetime = true;
			m_paused = false;
		}
		m_cv.notify_one();

		{
			std::unique_lock<std::mutex> lk(m_m);
			m_cv.wait(lk, [this]{return m_paused;});
		}

	}

	void wait_for_next_frame_signal(){
		// wait for the resume one time signal
		if(m_debug_mode){
			std::unique_lock<std::mutex> lk(m_m);
			m_paused = true;
			m_cv.notify_one();
			m_cv.wait(lk, [this]{return m_resume_onetime;});
			m_resume_onetime = false;
		}
	}
};

ThreadUtil thread_util;
void worker_thread1()
{
	std::cout << "thread1:  enter worker thread1\n";

	// Ask thread 2 to pause
	std::cout << "thread1: please pause\n";
	thread_util.pause_tracking();
	std::cout << "thread1: thread 2 now paused\n";


	//Ask thread 2 to resume once
	std::cout << "thread1: please resume\n";
	thread_util.track_next_frame();
	std::cout << "thread1: thread 2 now paused again\n";


	std::cout << "thread1: please resume2\n";
		thread_util.track_next_frame();
		std::cout << "thread1: thread 2 now paused again2\n";

	std::cout << "thread1: thread 1 exit\n";

}

void worker_thread2()
{
	std::cout << "enter worker thread2\n";
	while(true){
		thread_util.wait_for_next_frame_signal();
		std::cout << "worker thread2 executing\n";
		std::this_thread::sleep_for(std::chrono::milliseconds(100));
	}
}

int main()
{

	std::thread worker2(worker_thread2);
	std::this_thread::sleep_for(std::chrono::milliseconds(1000));
	std::thread worker1(worker_thread1);



	worker1.join();
	worker2.join();
}

