#include <iostream>
#include <pcl/io/pcd_io.h>
#include <pcl/point_types.h>

#define PCL_NO_PRECOMPILE
//#include <pcl/memory.h>
#include <pcl/pcl_macros.h>
#include <pcl/point_types.h>
#include <pcl/point_cloud.h>
#include <pcl/io/pcd_io.h>

struct VSlamPoint
{
  PCL_ADD_POINT4D;                  // preferred way of adding a XYZ+padding
  uint32_t id;
  EIGEN_MAKE_ALIGNED_OPERATOR_NEW     // make sure our new allocators are aligned
};                    // enforce SSE padding for correct memory alignment

POINT_CLOUD_REGISTER_POINT_STRUCT (VSlamPoint,           // here we assume a XYZ + "test" (as fields)
                                   (float, x, x)
                                   (float, y, y)
                                   (float, z, z)
                                   (uint32_t, id, id)
)



int
  main (int argc, char** argv)
{
  pcl::PointCloud<VSlamPoint> cloud;

  // Fill in the cloud data
  cloud.width    = 5;
  cloud.height   = 1;
  cloud.is_dense = false;
  cloud.points.resize (cloud.width * cloud.height);

  for (std::size_t i = 0; i < cloud.points.size (); ++i)
  {
    cloud.points[i].x = 1024 * rand () / (RAND_MAX + 1.0f);
    cloud.points[i].y = 1024 * rand () / (RAND_MAX + 1.0f);
    cloud.points[i].z = 1024 * rand () / (RAND_MAX + 1.0f);
    cloud.points[i].id = i;
  }

  pcl::PointXYZL p;
//  p.x = 1;
//  p.y = 2;
//  p.z = 3;
//  cloud.push_back(p);
  pcl::io::savePCDFileASCII ("test_pcd.pcd", cloud);
  std::cerr << "Saved " << cloud.points.size () << " data points to test_pcd.pcd." << std::endl;

  for (std::size_t i = 0; i < cloud.points.size (); ++i)
    std::cerr << "    " << cloud.points[i].x << " " << cloud.points[i].y << " " << cloud.points[i].z<< ", "<< cloud.points[i].id << std::endl;

  return (0);
}
