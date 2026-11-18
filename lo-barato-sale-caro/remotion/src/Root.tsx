import { Composition, Still } from "remotion";
import { PerfilInstagram } from "./PerfilInstagram";
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
      <Still
        id="PerfilAmarillo"
        component={PerfilInstagram}
        width={1080}
        height={1080}
        defaultProps={{ fondo: "#f2b600", fondoCentro: "#ffd84a" }}
      />
      <Still
        id="PerfilAzul"
        component={PerfilInstagram}
        width={1080}
        height={1080}
        defaultProps={{ fondo: "#141b36", fondoCentro: "#34457e" }}
      />
      <Composition id="Prueba" component={Prueba} durationInFrames={60} fps={30} width={1080} height={1920} />
    </>
  );
};
