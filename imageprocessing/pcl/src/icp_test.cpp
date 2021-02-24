#include <iostream>
#include <pcl/io/pcd_io.h>
#include <pcl/point_types.h>
#include <pcl/registration/icp.h>
using namespace Eigen;

Eigen::Matrix4f gettrans(){
	//Roll pitch and yaw in Radians
	float roll = 0.0, pitch = 0, yaw = 0.2;
	Quaternionf q;
	q = AngleAxisf(roll, Vector3f::UnitX())
	    * AngleAxisf(pitch, Vector3f::UnitY())
	    * AngleAxisf(yaw, Vector3f::UnitZ());
	std::cout << "Quaternion" << std::endl << q.coeffs() << std::endl;
	auto euler = q.toRotationMatrix().eulerAngles(0, 1, 2);
	std::cout << "Euler from quaternion in roll, pitch, yaw"<< std::endl << euler << std::endl;
	Matrix3f r = q.toRotationMatrix();
	Matrix4f res = Matrix4f::Identity();

	res.block<3,3>(0,0) = r;
	res(0,3) = 0.2;
	res(1,3) = 0.1;
	res(2,3) = 0.3;

	return res;
}


int
 main (int argc, char** argv)
{
  pcl::PointCloud<pcl::PointXYZ>::Ptr cloud_in (new pcl::PointCloud<pcl::PointXYZ>(5,1));
  pcl::PointCloud<pcl::PointXYZ>::Ptr cloud_out (new pcl::PointCloud<pcl::PointXYZ>);

  // Fill in the CloudIn data
  for (auto& point : *cloud_in)
  {
    point.x = 1024 * rand() / (RAND_MAX + 1.0f);
    point.y = 1024 * rand() / (RAND_MAX + 1.0f);
    point.z = 1024 * rand() / (RAND_MAX + 1.0f);
  }

  std::cout << "Saved " << cloud_in->size () << " data points to input:" << std::endl;

  for (auto& point : *cloud_in)
    std::cout << point << std::endl;

  *cloud_out = *cloud_in;

  std::cout << "size:" << cloud_out->size() << std::endl;

  Matrix4f trans;
  trans = gettrans();
  std::cout << "transformation matrix:\n"<<trans << std::endl;
  for (auto& point : *cloud_out){
	  Vector4f point_trans;
	  point_trans<<point.x, point.y, point.z, 1.0;
	  auto new_point = trans * point_trans;
	     point.x =new_point[0];
	     point.y =new_point[1];
	     point.z =new_point[2];
  }


  std::cout << "Transformed " << cloud_in->size () << " data points:" << std::endl;

  for (auto& point : *cloud_out)
    std::cout << point << std::endl;

  pcl::IterativeClosestPoint<pcl::PointXYZ, pcl::PointXYZ> icp;
  icp.setInputSource(cloud_in);
  icp.setInputTarget(cloud_out);

  pcl::PointCloud<pcl::PointXYZ> Final;
  icp.align(Final);

  std::cout << "has converged:" << icp.hasConverged() << " score: " <<
  icp.getFitnessScore() << std::endl;
  std::cout << icp.getFinalTransformation() << std::endl;

 return (0);
}
