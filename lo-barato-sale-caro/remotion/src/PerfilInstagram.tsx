import { loadFont } from "@remotion/fonts";
import { ThreeCanvas } from "@remotion/three";
import React from "react";
import { AbsoluteFill, staticFile, useVideoConfig } from "remotion";
import { Camara } from "./3d/Escenario";
import { Personaje } from "./3d/Personaje";

loadFont({ family: "Anton", url: staticFile("fuentes/anton-latin.woff2"), weight: "400" });

// Foto de perfil: el personaje de los videos con cara de desconfiado y una etiqueta de precio.
// Instagram la recorta en círculo y la muestra a ~110 px: nada importante cerca de las esquinas.
export const PerfilInstagram: React.FC<{ fondo: string; fondoCentro: string }> = ({ fondo, fondoCentro }) => {
  const { width, height } = useVideoConfig();
  return (
    <AbsoluteFill style={{ background: `radial-gradient(circle at 50% 42%, ${fondoCentro} 0%, ${fondo} 70%)` }}>
      <ThreeCanvas width={width} height={height} shadows gl={{ alpha: true, antialias: true }}>
        <Camara pos={[0.36, 1.3, 2.3]} mira={[0.1, 1.25, 0]} fov={31} />
        <hemisphereLight args={["#fff4e0", "#3a3f5c", 0.7]} />
        <directionalLight position={[2.5, 3.5, 3]} intensity={2.4} color="#fff1dc" />
        <directionalLight position={[-2.5, 2, -2]} intensity={2.2} color="#9fb4ff" />
        <pointLight position={[-1.2, 1.4, 1.8]} intensity={2.2} distance={5} color="#ffe7c2" />
        <Personaje cabezaGiro={0.14} cabezaInclina={-0.06} cejasLado={[-0.75, 0.95]} />
      </ThreeCanvas>
      {/* Etiqueta de precio */}
      <div
        style={{
          position: "absolute",
          left: 735,
          top: 255,
          rotate: "12deg",
          display: "flex",
          alignItems: "center",
          gap: 14,
          background: "#ff3b30",
          color: "#fbf8f1",
          fontFamily: "Anton",
          fontSize: 132,
          lineHeight: 1,
          padding: "10px 34px 18px 26px",
          borderRadius: "22px 34px 34px 22px",
          boxShadow: "0 12px 0 rgba(0,0,0,0.3)",
        }}
      >
        <div style={{ width: 30, height: 30, borderRadius: 15, background: "#fbf8f1", boxShadow: "inset 0 4px 0 rgba(0,0,0,0.25)" }} />
        $
      </div>
    </AbsoluteFill>
  );
};
