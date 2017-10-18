#include <iostream>
#include <algorithm>
#include <memory>
using namespace std;

class A
{
public:

	// Simple constructor that initializes the resource.
	explicit A(size_t length)
	: mLength(length), mData(new int[length])
	{
		std::cout << "A(size_t). length = "
				<< mLength << "." << std::endl;
	}

	// Destructor.
	~A()
	{
		std::cout << "~A(). length = " << mLength << ".";

//		if (mData != NULL) {
//			std::cout << " Deleting resource.";
//			delete[] mData;  // Delete the resource.
//		}

		std::cout << std::endl;
	}

//	// Copy constructor.
//	A(const A& other)
//	: mLength(other.mLength), mData(new int[other.mLength])
//	{
//		std::cout << "A(const A&). length = "
//				<< other.mLength << ". Copying resource." << std::endl;
//
//		std::copy(other.mData, other.mData + mLength, mData);
//	}
//
//	// Copy assignment operator.
//	A& operator=(const A& other)
//	{
//		std::cout << "operator=(const A&). length = "
//				<< other.mLength << ". Copying resource." << std::endl;
//
//		if (this != &other) {
//			delete[] mData;  // Free the existing resource.
//			mLength = other.mLength;
//			mData = new int[mLength];
//			std::copy(other.mData, other.mData + mLength, mData);
//		}
//		return *this;
//	}
//
//	// Move constructor.
//	A(A&& other)
//	{
//		std::cout << "A(A&&). length = "
//				<< other.mLength << ". Moving resource.\n";
//
//		// Copy the data pointer and its length from the
//		// source object.
//		mData = other.mData;
//		mLength = other.mLength;
//
//		// Release the data pointer from the source object so that
//		// the destructor does not free the memory multiple times.
//		other.mData = NULL;
//		other.mLength = 0;
//	}
//
//
//	// Move assignment operator.
//	A& operator=(A&& other)
//	{
//		std::cout << "operator=(A&&). length = "
//				<< other.mLength << "." << std::endl;
//
//		if (this != &other) {
//			// Free the existing resource.
//			delete[] mData;
//
//			// Copy the data pointer and its length from the
//			// source object.
//			mData = other.mData;
//			mLength = other.mLength;
//
//			// Release the data pointer from the source object so that
//			// the destructor does not free the memory multiple times.
//			other.mData = NULL;
//			other.mLength = 0;
//		}
//		return *this;
//	}

	void disp(){
		mvar = 100;
		std::cout<<"mvar "<< mvar<<std::endl;
	}
	// Retrieves the length of the data resource.
	size_t Length() const
	{
		return mLength;
	}

private:
	int mvar;
	size_t mLength; // The length of the resource.
	std::shared_ptr<int>  mData;     // The resource.
};

#include <vector>

A get_aobj(){
	A a(21);
	return a;
}

int main()
{
//	A temp = get_aobj();
//	temp.disp();
	// Create a vector object and add a few elements to it.
	std::vector<A> v;
	v.push_back(A(25));

//	std::vector<A> v2;
//	v2 = std::move(v);
//	v2 = static_cast<std::vector<A> &&>(v);
//	v2 = v;
//	v.push_back(A(75));

	// Insert a new element into the second position of the vector.
//	v.insert(v.begin(), A(50));
	return 0;
}
