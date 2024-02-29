#include <iostream>
#include <vector>
#include <memory>
using namespace std;


class Person {
    int _age;

public:
Person(){
        cout << "Construct a person, raw" << _age << endl;
    }
    Person(int age) : _age(age) {
        cout << "Construct a person." << _age << endl;
    }

    Person(const Person &p) : _age(p._age) {
        cout << "Copy-Construct" << _age << endl;
    }

    Person(const Person &&p) noexcept: _age(p._age) {
        cout << "Move-Construct" << _age << endl;
    }
	virtual ~Person(){
		cout << "deconstructor()" << _age << endl;
	}
};


int main() {
    
    vector<std::shared_ptr<Person>> person;
	auto p = std::make_shared<Person>(1);
	// person.emplace_back(2);
    // auto p = Person(1); // >: Construct a person.1
    person.push_back(p);
	// person.emplace_back(move(p)); // >: Move-Construct1
    /**
     * >: Copy-Construct1 因为容器扩容，需要把前面的元素重新添加进来，因此需要拷贝
     */
	return 0;
}