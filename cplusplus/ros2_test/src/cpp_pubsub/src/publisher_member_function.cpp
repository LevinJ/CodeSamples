#include <chrono>
#include <functional>
#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

#include <opencv2/opencv.hpp>
// #include "sensor_msgs/image_encodings.hpp"
#include "sensor_msgs/msg/compressed_image.hpp"
// #include "sensor_msgs/msg/image.hpp"

using namespace cv;


using namespace std::chrono_literals;

/* This example creates a subclass of Node and uses std::bind() to register a
* member function as a callback from the timer. */

class MinimalPublisher : public rclcpp::Node
{
  public:
    MinimalPublisher()
    : Node("minimal_publisher"), count_(0)
    {
      publisher_ = this->create_publisher<std_msgs::msg::String>("topic", 10);
      timer_ = this->create_wall_timer(
      500ms, std::bind(&MinimalPublisher::timer_callback, this));

        jpeg_pub_ =  this->create_publisher<sensor_msgs::msg::CompressedImage>("image_raw/compressed", 1);
    }

  private:
    void timer_callback()
    {
      auto message = std_msgs::msg::String();
      message.data = "Hello, world! " + std::to_string(count_++);
      RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", message.data.c_str());
      publisher_->publish(message);

        std::string img_file = "/home/levin/temp/1.bmp";
        Mat mat;
        mat = imread( img_file, 1 );

        unsigned char * buf_data = mat.data;

        auto img = std::make_unique<sensor_msgs::msg::CompressedImage>();
    // img->header = cinfo->header;
        img->format = "jpeg";
        int buf_size = mat.total() * mat.elemSize();
        img->data.resize(buf_size);
        std::copy(buf_data, (buf_data) + (buf_size), img->data.begin());
        jpeg_pub_->publish(std::move(img));

    }
    rclcpp::TimerBase::SharedPtr timer_;
    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
    size_t count_;
    rclcpp::Publisher<sensor_msgs::msg::CompressedImage>::SharedPtr jpeg_pub_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<MinimalPublisher>());
  rclcpp::shutdown();
  return 0;
}