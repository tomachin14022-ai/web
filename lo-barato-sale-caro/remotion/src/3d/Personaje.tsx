import React from "react";

// Personaje propio de "Lo barato sale caro": cabeza redonda blanca, ojos negros,
// cejas que marcan la emoción, remera amarilla. Todo se mueve por props (cuadro a cuadro).
export type Pose = {
  readonly x?: number;
  readonly z?: number;
  readonly giro?: number; // giro del cuerpo (rad)
  readonly cabezaGiro?: number; // + mira a su izquierda (a la derecha de la pantalla)
  readonly cabezaInclina?: number;
  readonly cabezaArriba?: number; // + mira hacia arriba
  readonly cejas?: number; // -1 enojado · 0 normal · 1 sorprendido
  readonly parpadeo?: number; // 0 abierto · 1 cerrado
  readonly brazoDer?: number; // 0 abajo · 1 apuntando al frente
  readonly brazoIzq?: number;
  readonly respira?: number; // fase en radianes
  readonly salto?: number; // altura extra (m)
  readonly escala?: number;
  readonly remera?: string;
};

const PIEL = "#f3efe6";
const NEGRO = "#16161a";
const PANTALON = "#262b3d";

const Brazo: React.FC<{ lado: 1 | -1; alza: number; remera: string }> = ({ lado, alza, remera }) => {
  // Pivote en el hombro; alza 0 = colgando, 1 = apuntando al frente, 1,7 = brazo arriba
  const rotX = -alza * 1.75;
  const rotZ = lado * (0.12 + alza * 0.25);
  return (
    <group position={[lado * 0.25, 1.02, 0]} rotation={[rotX, 0, rotZ]}>
      <mesh position={[0, -0.13, 0]} castShadow>
        <capsuleGeometry args={[0.075, 0.14, 8, 16]} />
        <meshStandardMaterial color={remera} roughness={0.75} />
      </mesh>
      <mesh position={[0, -0.33, 0]} castShadow>
        <capsuleGeometry args={[0.055, 0.16, 8, 16]} />
        <meshStandardMaterial color={PIEL} roughness={0.6} />
      </mesh>
      <mesh position={[0, -0.47, 0]} castShadow>
        <sphereGeometry args={[0.07, 20, 20]} />
        <meshStandardMaterial color={PIEL} roughness={0.6} />
      </mesh>
    </group>
  );
};

export const Personaje: React.FC<Pose> = ({
  x = 0,
  z = 0,
  giro = 0,
  cabezaGiro = 0,
  cabezaInclina = 0,
  cabezaArriba = 0,
  cejas = 0,
  parpadeo = 0,
  brazoDer = 0,
  brazoIzq = 0,
  respira = 0,
  salto = 0,
  escala = 1,
  remera = "#ffcc00",
}) => {
  const aire = Math.sin(respira) * 0.012;
  const ojoY = 1 - parpadeo * 0.9;
  // Cejas: sorprendido = arriba y rectas; enojado = abajo e inclinadas hacia adentro
  const cejaY = 1.535 + cejas * 0.04;
  const cejaRot = cejas < 0 ? -cejas * 0.45 : -cejas * 0.12;
  return (
    <group position={[x, salto, z]} rotation={[0, giro, 0]} scale={escala}>
      {/* Piernas y zapatos */}
      {[-1, 1].map((l) => (
        <group key={l} position={[l * 0.11, 0, 0]}>
          <mesh position={[0, 0.34, 0]} castShadow>
            <capsuleGeometry args={[0.085, 0.4, 8, 16]} />
            <meshStandardMaterial color={PANTALON} roughness={0.8} />
          </mesh>
          <mesh position={[0, 0.05, 0.05]} castShadow>
            <boxGeometry args={[0.15, 0.09, 0.26]} />
            <meshStandardMaterial color={NEGRO} roughness={0.5} />
          </mesh>
        </group>
      ))}
      {/* Torso con remera */}
      <group position={[0, aire, 0]} scale={[1, 1 + aire * 2, 1]}>
        <mesh position={[0, 0.84, 0]} castShadow>
          <capsuleGeometry args={[0.215, 0.3, 10, 24]} />
          <meshStandardMaterial color={remera} roughness={0.75} />
        </mesh>
        <Brazo lado={1} alza={brazoDer} remera={remera} />
        <Brazo lado={-1} alza={brazoIzq} remera={remera} />
      </group>
      {/* Cabeza */}
      <group position={[0, 1.36 + aire, 0]} rotation={[-cabezaArriba, cabezaGiro, cabezaInclina]}>
        <mesh castShadow scale={[1, 1.04, 0.98]}>
          <sphereGeometry args={[0.31, 48, 48]} />
          <meshStandardMaterial color={PIEL} roughness={0.55} />
        </mesh>
        {[-1, 1].map((l) => (
          <group key={l}>
            {/* Ojo */}
            <mesh position={[l * 0.105, 0.05, 0.285]} scale={[0.8, 1.3 * ojoY + 0.05, 0.45]}>
              <sphereGeometry args={[0.048, 20, 20]} />
              <meshStandardMaterial color={NEGRO} roughness={0.25} />
            </mesh>
            {/* Brillo del ojo */}
            <mesh position={[l * 0.105 + 0.012, 0.075, 0.305]} scale={ojoY}>
              <sphereGeometry args={[0.011, 10, 10]} />
              <meshBasicMaterial color="#ffffff" />
            </mesh>
            {/* Ceja */}
            <mesh position={[l * 0.11, cejaY - 1.36, 0.27]} rotation={[-0.25, 0, l * cejaRot]}>
              <boxGeometry args={[0.12, 0.026, 0.03]} />
              <meshStandardMaterial color={NEGRO} roughness={0.4} />
            </mesh>
          </group>
        ))}
      </group>
    </group>
  );
};
