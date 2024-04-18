import { Swiper, SwiperSlide } from "swiper/react";
import { Navigation, Autoplay } from "swiper/modules";

import "swiper/css";
import "swiper/css/navigation";

const Carousel = () => {
  return (
    <div className=" bg-black  flex items-center -z-[3000] ">
      <Swiper
        loop={true}
        spaceBetween={0}
        navigation={true}
        modules={[Navigation, Autoplay]}
        autoplay={{
          delay: 10000,
        }}
        className="h-[200px]"
      >
        <SwiperSlide className="bg-black">
          <video
            className="w-full h-full object-cover"
            controls
            muted="muted"
            autoPlay
            loop
          >
            <source src="./images/v6.mp4" type="video/mp4" />
          </video>
        </SwiperSlide>
        <SwiperSlide className="bg-black">
          <video
            className="w-full h-full object-cover"
            controls
            muted="muted"
            autoPlay
            loop
          >
            <source src="./images/v3.mp4" type="video/mp4" />
          </video>
        </SwiperSlide>
        <SwiperSlide className="bg-black">
          <video
            className="w-full h-full object-cover"
            controls
            muted="muted"
            autoPlay
            loop
          >
            <source src="./images/v4.mp4" type="video/mp4" />
          </video>
        </SwiperSlide>
        <SwiperSlide className="bg-black">
          <video
            className="w-full h-full object-cover"
            controls
            muted="muted"
            autoPlay
            loop
          >
            <source src="./images/v5.mp4" type="video/mp4" />
          </video>
        </SwiperSlide>
      </Swiper>
    </div>
  );
};

export default Carousel;