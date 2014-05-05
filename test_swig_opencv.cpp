#include "test_swig_opencv.hpp"

#include <opencv2/imgproc/imgproc.hpp>

void UsefulStuffUsingOpenCV::doit(cv::Mat& input) {
  // Draw a circle
  cv::circle(input, cv::Point2f(input.cols/2, input.rows/2), input.cols/5, 0, -1);
}
