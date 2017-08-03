#include <iostream>
#include <chrono>
using namespace std;

class ElapsedClock
{
public:
    ElapsedClock() : beg_(clock_::now()) {}
    void reset() { beg_ = clock_::now(); }
    double elapsed() const {
        return std::chrono::duration_cast<chrono::milliseconds>
            (clock_::now() - beg_).count(); }

private:
    typedef std::chrono::high_resolution_clock clock_;

    std::chrono::time_point<clock_> beg_;
};

int main()
{
	cout << chrono::high_resolution_clock::period::den << endl;
	auto start_time = chrono::high_resolution_clock::now();
	ElapsedClock tmr;
	int temp;
	for (int i = 0; i< 24200000; i++)
		temp+=temp;
	auto end_time = chrono::high_resolution_clock::now();
	cout << chrono::duration_cast<chrono::seconds>(end_time - start_time).count() << ":";
	cout << chrono::duration_cast<chrono::microseconds>(end_time - start_time).count() << ":"<<endl;
	cout << chrono::duration_cast<chrono::milliseconds>(end_time - start_time).count() << endl;

	cout << "timer elapsed, " << tmr.elapsed()<<endl;
	return 0;
}
