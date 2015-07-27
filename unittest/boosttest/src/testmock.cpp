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
};

class calculator
{
public:
    calculator( view& v ){
    m_v = &v;
    }

    void add( int a, int b ){
    	m_v->display(a+b);
    }
private:
view *m_v;
    
};

MOCK_BASE_CLASS( mock_view, view ) // declare a 'mock_view' class implementing 'view'
{
    MOCK_METHOD( display, 1 )      // implement the 'display' method from 'view' (taking 1 argument)
};

BOOST_AUTO_TEST_CASE( zero_plus_zero_is_zero )
{
    mock_view v;
    calculator c( v );
    MOCK_EXPECT( v.display ).once().with( 0 ); // expect the 'display' method to be called once (and only once) with a parameter value equal to 0
    c.add( 0, 0 );
}