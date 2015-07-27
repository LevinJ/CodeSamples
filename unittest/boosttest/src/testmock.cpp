#include <boost/test/unit_test.hpp>
#include <turtle/mock.hpp>

BOOST_AUTO_TEST_CASE(universeInOrder22)
{
    BOOST_CHECK(6 == 5);
}

class view
{
public:
    virtual void display( int result ) = 0;
    virtual int display2( int result ) = 0;
};

class calculator
{
public:
    calculator( view& v ){
    m_v = &v;
    }

    void add( int a, int b ){
    	m_v->display(a+b);
    	m_v->display2(a+b);
    }
private:
view *m_v;
    
};

MOCK_BASE_CLASS( mock_view, view ) // declare a 'mock_view' class implementing 'view'
{
    MOCK_METHOD( display, 1 )      // implement the 'display' method from 'view' (taking 1 argument)
	MOCK_METHOD( display2, 1 )
};
int function( int i )
{
    return i;
}

//BOOST_AUTO_TEST_CASE( zero_plus_zero_is_zero )
//{
//    mock_view v;
//    calculator c( v );
//    MOCK_EXPECT( v.display ).once().with( 0 ); // expect the 'display' method to be called once (and only once) with a parameter value equal to 0
//    c.add( 0, 0 );
//    MOCK_VERIFY( v.display );                  // verify all expectations are fulfilled for the 'display' method
//        mock::verify( v );                         // verify all expectations are fulfilled for all methods of 'v'
//        mock::verify();                            // verify all expectations are fulfilled for all existing mock objects
//        MOCK_RESET( v.display );                   // reset all expectations for the 'display' method
//        mock::reset( v );                          // reset all expectations for all methods of 'v'
//        mock::reset();
//}

BOOST_AUTO_TEST_CASE( zero_plus_zero_is_zero2 )
{
    mock_view v;
    calculator c( v );
    MOCK_EXPECT( v.display ).once().with( 0 ); // this call must occur once (and only once)
    MOCK_EXPECT( v.display2 ).once().with( 0 ).returns(0);
//    MOCK_EXPECT( v.display ).once().with( 1 );        // this call can occur any number of times (including never)
    c.add( 0, 0 );
    //c.add( 2, 0 );
}
