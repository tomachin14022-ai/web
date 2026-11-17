import { ThreeCanvas } from "@remotion/three";
import React from "react";
import { AbsoluteFill, useCurrentFrame, useVideoConfig } from "remotion";
import { Camara, Escenario } from "./3d/Escenario";
import { Personaje } from "./3d/Personaje";
import { Podio, Producto } from "./3d/Productos";

// Boceto para revisar el look del personaje, los productos y la luz
export const Prueba: React.FC = () => {
  const frame = useCurrentFrame();
  const { width, height } = useVideoConfig();
  return (
    <AbsoluteFill>
      <ThreeCanvas width={width} height={height} shadows>
        <Camara pos={[0, 1.55, 6.2]} mira={[0, 1.0, 0]} fov={34} />
        <Escenario frame={frame} pared="#1d2748" piso="#2a3459" contraluz="#6f8cff" />
        <group position={[-0.95, 0, -0.3]}>
          <Podio color="#e8221b" />
          <group position={[0, 0.55, 0]}>
            <Producto tipo="cafetera-capsulas" />
          </group>
        </group>
        <group position={[0.95, 0, -0.3]}>
          <Podio color="#ffcc00" />
          <group position={[0, 0.55, 0]}>
            <Producto tipo="cafetera-espresso" />
          </group>
        </group>
        <Personaje z={0.5} cabezaGiro={-0.35} cejas={-0.8} brazoDer={0.0} respira={frame / 12} />
      </ThreeCanvas>
    </AbsoluteFill>
  );
};
