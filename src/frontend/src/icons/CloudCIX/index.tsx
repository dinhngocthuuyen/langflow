import React, { forwardRef } from "react";
import cixBlue from "./CIX_Blue.png";  // Import the PNG image

export const CloudCIXIcon = forwardRef<
  HTMLImageElement,
  React.PropsWithChildren<{}>
>((props, ref) => {
  return (
    <img
      ref={ref}
      src={cixBlue}
      alt="CloudCIX Icon"
      {...props}
      style={{
        objectFit: "contain",
        border: "2px 0",
      }}
    />
  );
});
