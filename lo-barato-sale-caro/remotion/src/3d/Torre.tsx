import { RoundedBox } from "@react-three/drei";
import React from "react";

const FAJO = 0.07; // alto de cada fajo de billetes (m)

// Pila de fajos de billetes de la altura pedida; el de arriba se va completando
export const Torre: React.FC<{ alto: number; color: string }> = ({ alto, color }) => {
  const enteros = Math.floor(alto / FAJO);
  const resto = alto / FAJO - enteros;
  const fajos = Array.from({ length: enteros + (resto > 0.02 ? 1 : 0) });
  return (
    <group>
      {fajos.map((_, i) => {
        const parcial = i === enteros ? resto : 1;
        const giro = Math.sin(i * 2.3) * 0.08;
        const corrido = Math.sin(i * 1.7) * 0.015;
        return (
          <group key={i} position={[corrido, i * FAJO + (FAJO * parcial) / 2, 0]} rotation={[0, giro, 0]} scale={[1, parcial, 1]}>
            <RoundedBox args={[0.56, FAJO * 0.94, 0.28]} radius={0.012} smoothness={2} castShadow receiveShadow>
              <meshStandardMaterial color={color} roughness={0.75} />
            </RoundedBox>
            {/* Faja de papel */}
            <mesh>
              <boxGeometry args={[0.09, FAJO * 0.96, 0.285]} />
              <meshStandardMaterial color="#f6f1e2" roughness={0.8} />
            </mesh>
          </group>
        );
      })}
    </group>
  );
};
