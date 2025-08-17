import React, { useRef } from "react";
import videoPlayIcon from "./../../../../assets/images/pages/workspace/video_play_icon.svg";

interface VideoItemProps {
  src: string;
}

const VideoItem: React.FC<VideoItemProps> = ({ src }) => {
  const videoRef = useRef<HTMLVideoElement>(null);
  const [isPlaying, setIsPlaying] = React.useState(false);

  // function fetchVideoAndPlay() {
  //   fetch(src)
  //     // .then((response) => response.blob())
  //     .then((blob) => {
  //       // videoRef.current.srcObject = blob;
  //       return videoRef.current.play();
  //     })
  //     .then((_) => {
  //       // Video playback started ;)
  //     })
  //     .catch((e) => {
  //       // Video playback failed ;(
  //     });
  // }
  const handleMouseOver = () => {
    if (videoRef.current && videoRef.current.paused) {
      // This will allow us to play video later...
      // videoRef.current.load();
      // videoRef.current.play();

      // Show loading animation.
      var playPromise = videoRef.current.play();

      if (playPromise !== undefined) {
        playPromise
          .then((_) => {
            // Automatic playback started!
            // Show playing UI.
          })
          .catch((error) => {
            // Auto-play was prevented
            // Show paused UI.
          });
      }
      setIsPlaying(true);
    }
  };

  const handleMouseOut = () => {
    if (videoRef.current && !videoRef.current.paused) {
      videoRef.current.pause();
      setIsPlaying(false);
    }
  };

  // React.useEffect(() => {
  //   const video = videoRef.current;
  //   if (video) {
  //     const handlePlay = () => console.log("Video is playing");
  //     const handlePause = () => console.log("Video is paused");

  //     video.addEventListener("play", handlePlay);
  //     video.addEventListener("pause", handlePause);

  //     return () => {
  //       video.removeEventListener("play", handlePlay);
  //       video.removeEventListener("pause", handlePause);
  //     };
  //   }
  // }, []);
  return (
    <>
      <video
        ref={videoRef}
        // autoPlay
        loop
        // 加上muted属性，否则无法自动播放
        muted
        playsInline
        className="w-full h-full object-cover"
        onMouseOver={handleMouseOver}
        onMouseOut={handleMouseOut}
        controls={false}
      >
        <source src={src} type="video/mp4" />
        {/* <source src={src} type="video/webm" /> */}
      </video>
      {!isPlaying ? (
        <div className="border border-white rounded-full p-1 absolute top-2 right-2 transition-all duration-300 ease-in-out opacity-100">
          <img
            src={videoPlayIcon}
          />
        </div>
      ) : null}
    </>
  );
};

export default VideoItem;
