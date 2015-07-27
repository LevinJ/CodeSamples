#include "gtest/gtest.h"

#include "gmock/gmock.h"  // Brings in Google Mock.



class MassiveTest : public ::testing::Test
{
public:
	MassiveTest()
	    {
	//        BOOST_TEST_MESSAGE("setup mass");
		 m = 2;
	    }

	    ~MassiveTest()
	    {
	//        BOOST_TEST_MESSAGE("teardown mass");
	    }
protected:
    int m;
};
TEST_F(MassiveTest, IsEmptyInitially) {
  EXPECT_EQ(m, 2);
  m = m+1;
  EXPECT_EQ(m, 4);
}



