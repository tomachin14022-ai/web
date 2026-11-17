import { Composition } from "remotion";
import { Prueba } from "./Prueba";
import { VideoComparacion } from "./VideoComparacion";

// Duración = fin de cada video (datos/videos.ts) × 30 fps
export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="Cafetera"
        component={VideoComparacion}
        durationInFrames={672}
        fps={30}
        width={1080}
        height={1920}
        defaultProps={{ video: "cafetera" }}
      />
      <Composition
        id="Impresora"
        component={VideoComparacion}
        durationInFrames={678}
        fps={30}
        width={1080}
        height={1920}
        defaultProps={{ video: "impresora" }}
      />
      <Composition
        id="Aire"
        component={VideoComparacion}
        durationInFrames={702}
        fps={30}
        width={1080}
        height={1920}
        defaultProps={{ video: "aire" }}
      />
      <Composition id="Prueba" component={Prueba} durationInFrames={60} fps={30} width={1080} height={1920} />
    </>
  );
};
