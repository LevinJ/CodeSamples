////============================================================================
//// Name        : googleTest.cpp
//// Author      :
//// Version     :
//// Copyright   : Your copyright notice
//// Description : Hello World in C++, Ansi-style
////============================================================================
//
//#include <iostream>
//using namespace std;
//
//int main() {
//	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
//	return 0;
//}


#include "gtest/gtest.h"

#include "gmock/gmock.h"  // Brings in Google Mock.

using ::testing::AtLeast;


class Turtle {
public:
  virtual ~Turtle() {}
  virtual void PenUp() = 0;
  virtual void PenDown() = 0;
  virtual void Forward(int distance) = 0;
  virtual void Turn(int degrees) = 0;
  virtual void GoTo(int x, int y) = 0;
  virtual int GetX() const = 0;
  virtual int GetY() const = 0;
};


class MockTurtle : public Turtle {
 public:
  MOCK_METHOD0(PenUp, void());
  MOCK_METHOD0(PenDown, void());
  MOCK_METHOD1(Forward, void(int distance));
  MOCK_METHOD1(Turn, void(int degrees));
  MOCK_METHOD2(GoTo, void(int x, int y));
  MOCK_CONST_METHOD0(GetX, int());
  MOCK_CONST_METHOD0(GetY, int());
};


// Tests factorial of 0.
TEST(FactorialTesty, HandlesZeroInput) {
  EXPECT_EQ(1, 0);
}

class Painter{
public:
	Painter(const Turtle *t_){};
	bool DrawCircle(int x, int y, int z){
		return true;
	}
};
TEST(PainterTest, CanDrawSomething) {
  MockTurtle turtle;                          // #2
  EXPECT_CALL(turtle, PenDown())              // #3
      .Times(AtLeast(1));

  Painter painter(&turtle);                   // #4

  EXPECT_TRUE(painter.DrawCircle(0, 0, 10));
}

