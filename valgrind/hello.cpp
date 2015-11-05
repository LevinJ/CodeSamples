#include <stdlib.h>
#include <stdio.h>
  class TestClass2
  {
    int *m_arr;
  public:
    TestClass2(){
      m_arr = new int(1000);
    };
    ~TestClass2(){};
    
  };
  class TestClass
  {
  public:
    int m_i;
    bool m_b;
    TestClass2 *m_pi;
    TestClass(){
      m_i = 1000;
      m_b = true;
      m_pi = new TestClass2();
    };
    void printit(){
      printf("We should not see this line...\n");
    }
    void Leakit(){
      TestClass2 *p = new TestClass2();
    }
    ~TestClass(){};
    
  };

  void MemoryLeak(){
    TestClass *obj1 = new TestClass();
  }
//Valgrind can detect  variable access of freed object
//Valgrind can not detect method access of freed object
  void AccessFreedObject(){
    TestClass *pObj = new TestClass();
    printf("vow %d  \n", pObj->m_i);
    delete pObj;
    pObj->printit();
    printf("vow %d  \n", pObj->m_i);
    pObj->printit();
  }
  int main(void)
  {
    printf("Here we start the call...\n");
    MemoryLeak();
    //AccessFreedObject();
    printf("Here we end the call...\n");
    return 0;
  }