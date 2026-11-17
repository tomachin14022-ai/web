import { useThree } from "@react-three/fiber";
import React, { useLayoutEffect } from "react";
import * as THREE from "three";

export type Vec3 = [number, number, number];
export type Toma = { pos: Vec3; mira: Vec3; fov: number };

// Cámara manejada por cuadro (sin useFrame): la posición sale de props
export const Camara: React.FC<Toma> = ({ pos, mira, fov }) => {
  const camera = useThree((s) => s.camera) as THREE.PerspectiveCamera;
  useLayoutEffect(() => {
    camera.position.set(pos[0], pos[1], pos[2]);
    camera.fov = fov;
    camera.near = 0.1;
    camera.far = 60;
    camera.lookAt(mira[0], mira[1], mira[2]);
    camera.updateProjectionMatrix();
  });
  return null;
};

// Proyecta un punto 3D a píxeles de pantalla con la misma toma que la cámara
export const proyectar = (p: Vec3, toma: Toma, ancho: number, alto: number): { x: number; y: number } => {
  const cam = new THREE.PerspectiveCamera(toma.fov, ancho / alto, 0.1, 60);
  cam.position.set(...toma.pos);
  cam.lookAt(...toma.mira);
  cam.updateMatrixWorld();
  cam.updateProjectionMatrix();
  const v = new THREE.Vector3(...p).project(cam);
  return { x: ((v.x + 1) / 2) * ancho, y: ((1 - v.y) / 2) * alto };
};

// Pseudoaleatorio determinista (sin Math.random)
const azar = (i: number) => {
  const s = Math.sin(i * 127.1 + 311.7) * 43758.5453;
  return s - Math.floor(s);
};

// Estudio: pared de fondo, piso, luces de cine y papelitos flotando
export const Escenario: React.FC<{ frame: number; pared: string; piso: string; contraluz: string }> = ({
  frame,
  pared,
  piso,
  contraluz,
}) => {
  return (
    <>
      <color attach="background" args={[pared]} />
      <fog attach="fog" args={[pared, 9, 22]} />
      <hemisphereLight args={["#fff4e0", piso, 0.55]} />
      <directionalLight
        position={[3.5, 6, 5]}
        intensity={2.1}
        color="#fff1dc"
        castShadow
        shadow-mapSize-width={1024}
        shadow-mapSize-height={1024}
        shadow-camera-left={-5}
        shadow-camera-right={5}
        shadow-camera-top={5}
        shadow-camera-bottom={-3}
        shadow-bias={-0.0005}
        shadow-radius={6}
      />
      {/* Contraluz de color para recortar las siluetas del fondo */}
      <directionalLight position={[-4, 3, -4]} intensity={1.6} color={contraluz} />
      <pointLight position={[0, 2.6, 2.2]} intensity={6} distance={7} color="#ffe7c2" />
      {/* Piso */}
      <mesh rotation={[-Math.PI / 2, 0, 0]} receiveShadow>
        <planeGeometry args={[40, 40]} />
        <meshStandardMaterial color={piso} roughness={0.85} />
      </mesh>
      {/* Pared de fondo con zócalo */}
      <mesh position={[0, 5, -3.2]} receiveShadow>
        <planeGeometry args={[40, 10]} />
        <meshStandardMaterial color={pared} roughness={0.95} />
      </mesh>
      <mesh position={[0, 0.08, -3.15]}>
        <boxGeometry args={[40, 0.16, 0.08]} />
        <meshStandardMaterial color={piso} roughness={0.7} />
      </mesh>
      {/* Papelitos que flotan (determinista) */}
      {Array.from({ length: 26 }).map((_, i) => {
        const t = frame / 30;
        const x = (azar(i) - 0.5) * 7;
        const y = 0.4 + ((azar(i + 50) * 4 + t * (0.08 + azar(i + 9) * 0.1)) % 4);
        const z = -2.6 + azar(i + 99) * 3.2;
        return (
          <mesh
            key={i}
            position={[x + Math.sin(t * 0.7 + i) * 0.15, y, z]}
            rotation={[t * (0.5 + azar(i + 3)), t * 0.3 + i, azar(i + 7) * 3]}
          >
            <planeGeometry args={[0.07, 0.05]} />
            <meshStandardMaterial color="#f3efe6" side={THREE.DoubleSide} roughness={0.9} transparent opacity={0.55} />
          </mesh>
        );
      })}
    </>
  );
};
