import { RoundedBox } from "@react-three/drei";
import React from "react";

// Productos de juguete, sin marcas: se reconocen por la forma, no por el logo.
export type TipoProducto =
  | "cafetera-capsulas"
  | "cafetera-espresso"
  | "impresora-cartucho"
  | "impresora-tanque"
  | "aire-comun"
  | "aire-inverter";

const Mat: React.FC<{ c: string; r?: number; m?: number; e?: string; ei?: number }> = ({ c, r = 0.5, m = 0, e, ei = 0 }) => (
  <meshStandardMaterial color={c} roughness={r} metalness={m} emissive={e ?? "#000000"} emissiveIntensity={ei} />
);

const Taza: React.FC<{ position: [number, number, number]; escala?: number }> = ({ position, escala = 1 }) => (
  <group position={position} scale={escala}>
    <mesh castShadow position={[0, 0.045, 0]}>
      <cylinderGeometry args={[0.05, 0.04, 0.09, 24]} />
      <Mat c="#fbfaf7" r={0.35} />
    </mesh>
    <mesh position={[0, 0.088, 0]}>
      <cylinderGeometry args={[0.044, 0.044, 0.005, 24]} />
      <Mat c="#3a2216" r={0.3} />
    </mesh>
    <mesh position={[0.058, 0.05, 0]} rotation={[Math.PI / 2, 0, 0]}>
      <torusGeometry args={[0.022, 0.008, 8, 16]} />
      <Mat c="#fbfaf7" r={0.35} />
    </mesh>
  </group>
);

const CafeteraCapsulas: React.FC = () => (
  <group>
    {/* Cuerpo angosto y alto */}
    <RoundedBox args={[0.3, 0.5, 0.46]} radius={0.06} smoothness={4} position={[0, 0.25, -0.02]} castShadow receiveShadow>
      <Mat c="#202126" r={0.3} />
    </RoundedBox>
    {/* Tapa con palanca */}
    <RoundedBox args={[0.31, 0.06, 0.3]} radius={0.025} smoothness={3} position={[0, 0.53, 0.03]} castShadow>
      <Mat c="#3a3c44" r={0.25} />
    </RoundedBox>
    {/* Boquilla */}
    <mesh position={[0, 0.39, 0.22]} castShadow>
      <cylinderGeometry args={[0.035, 0.035, 0.06, 20]} />
      <Mat c="#8d9099" r={0.3} m={0.5} />
    </mesh>
    {/* Bandeja */}
    <RoundedBox args={[0.28, 0.04, 0.2]} radius={0.015} smoothness={3} position={[0, 0.07, 0.25]} castShadow receiveShadow>
      <Mat c="#55585f" r={0.4} />
    </RoundedBox>
    <Taza position={[0, 0.09, 0.27]} escala={0.9} />
  </group>
);

const CafeteraEspresso: React.FC = () => (
  <group>
    {/* Cuerpo ancho de acero */}
    <RoundedBox args={[0.58, 0.6, 0.48]} radius={0.05} smoothness={4} position={[0, 0.3, -0.04]} castShadow receiveShadow>
      <Mat c="#c7cbd2" r={0.28} m={0.45} />
    </RoundedBox>
    {/* Frente negro con manómetro */}
    <RoundedBox args={[0.5, 0.2, 0.02]} radius={0.008} smoothness={2} position={[0, 0.48, 0.21]}>
      <Mat c="#1d1e22" r={0.3} />
    </RoundedBox>
    <mesh position={[0.15, 0.48, 0.225]} rotation={[Math.PI / 2, 0, 0]}>
      <cylinderGeometry args={[0.055, 0.055, 0.012, 32]} />
      <Mat c="#f4f2ec" r={0.3} />
    </mesh>
    <mesh position={[0.15, 0.48, 0.233]} rotation={[0, 0, -0.6]}>
      <boxGeometry args={[0.006, 0.045, 0.004]} />
      <Mat c="#e8221b" />
    </mesh>
    {/* Grupo y portafiltro con mango */}
    <mesh position={[-0.05, 0.33, 0.24]} castShadow>
      <cylinderGeometry args={[0.07, 0.07, 0.07, 28]} />
      <Mat c="#9ea3ab" r={0.25} m={0.6} />
    </mesh>
    <mesh position={[-0.05, 0.33, 0.39]} rotation={[Math.PI / 2, 0, 0]} castShadow>
      <capsuleGeometry args={[0.025, 0.2, 6, 12]} />
      <Mat c="#17181b" r={0.4} />
    </mesh>
    {/* Bandeja y taza */}
    <RoundedBox args={[0.5, 0.05, 0.22]} radius={0.015} smoothness={3} position={[0, 0.06, 0.27]} castShadow receiveShadow>
      <Mat c="#8d9199" r={0.3} m={0.5} />
    </RoundedBox>
    <Taza position={[-0.05, 0.085, 0.27]} />
    {/* Bandeja calientatazas arriba */}
    <RoundedBox args={[0.5, 0.025, 0.36]} radius={0.01} smoothness={2} position={[0, 0.61, -0.04]}>
      <Mat c="#a9aeb6" r={0.3} m={0.5} />
    </RoundedBox>
  </group>
);

const Hoja: React.FC<{ position: [number, number, number]; rot?: number }> = ({ position, rot = 0 }) => (
  <mesh position={position} rotation={[rot, 0, 0]} castShadow>
    <boxGeometry args={[0.3, 0.004, 0.4]} />
    <Mat c="#ffffff" r={0.9} />
  </mesh>
);

const ImpresoraCartucho: React.FC = () => (
  <group>
    <RoundedBox args={[0.68, 0.24, 0.44]} radius={0.04} smoothness={4} position={[0, 0.12, 0]} castShadow receiveShadow>
      <Mat c="#e9eaee" r={0.45} />
    </RoundedBox>
    {/* Escáner (tapa gris oscuro) */}
    <RoundedBox args={[0.66, 0.04, 0.42]} radius={0.015} smoothness={3} position={[0, 0.255, 0]} castShadow>
      <Mat c="#55585f" r={0.35} />
    </RoundedBox>
    {/* Bandeja de papel atrás */}
    <Hoja position={[0, 0.36, -0.25]} rot={-1.1} />
    {/* Salida */}
    <Hoja position={[0, 0.05, 0.3]} />
    <mesh position={[0, 0.1, 0.221]}>
      <boxGeometry args={[0.42, 0.03, 0.01]} />
      <Mat c="#2a2c31" />
    </mesh>
  </group>
);

const ImpresoraTanque: React.FC = () => (
  <group>
    <RoundedBox args={[0.72, 0.26, 0.48]} radius={0.04} smoothness={4} position={[-0.04, 0.13, 0]} castShadow receiveShadow>
      <Mat c="#1f2025" r={0.35} />
    </RoundedBox>
    <RoundedBox args={[0.7, 0.04, 0.46]} radius={0.015} smoothness={3} position={[-0.04, 0.275, 0]} castShadow>
      <Mat c="#2e3036" r={0.3} />
    </RoundedBox>
    {/* Bloque de tanques al costado, con 4 ventanitas de tinta */}
    <RoundedBox args={[0.14, 0.2, 0.3]} radius={0.02} smoothness={3} position={[0.38, 0.1, 0.06]} castShadow>
      <Mat c="#26282e" r={0.35} />
    </RoundedBox>
    {["#141414", "#18b7d8", "#d6268a", "#f2cf1f"].map((c, i) => (
      <mesh key={c} position={[0.3 + 0.0, 0.1, -0.05 + i * 0.065]} rotation={[0, Math.PI / 2, 0]}>
        <boxGeometry args={[0.045, 0.13, 0.012]} />
        <Mat c={c} r={0.2} e={c} ei={0.15} />
      </mesh>
    ))}
    <Hoja position={[-0.04, 0.38, -0.26]} rot={-1.1} />
    <Hoja position={[-0.04, 0.05, 0.31]} />
  </group>
);

const Aire: React.FC<{ inverter: boolean }> = ({ inverter }) => (
  <group>
    <RoundedBox args={[1.0, 0.3, 0.24]} radius={0.06} smoothness={4} position={[0, 0.15, 0]} castShadow receiveShadow>
      <Mat c="#f6f6f3" r={0.35} />
    </RoundedBox>
    {/* Salida de aire */}
    <RoundedBox args={[0.86, 0.05, 0.03]} radius={0.015} smoothness={2} position={[0, 0.04, 0.115]}>
      <Mat c="#3a3d44" r={0.6} />
    </RoundedBox>
    {/* Display */}
    <mesh position={[0.32, 0.2, 0.121]}>
      <boxGeometry args={[0.1, 0.035, 0.005]} />
      <Mat c={inverter ? "#29b6ff" : "#7d8088"} e={inverter ? "#29b6ff" : "#000000"} ei={inverter ? 1.4 : 0} />
    </mesh>
    {inverter ? (
      <mesh position={[0, 0.27, 0.121]}>
        <boxGeometry args={[0.7, 0.008, 0.004]} />
        <Mat c="#29b6ff" e="#29b6ff" ei={1.2} />
      </mesh>
    ) : null}
  </group>
);

export const Producto: React.FC<{ tipo: TipoProducto }> = ({ tipo }) => {
  switch (tipo) {
    case "cafetera-capsulas":
      return <CafeteraCapsulas />;
    case "cafetera-espresso":
      return <CafeteraEspresso />;
    case "impresora-cartucho":
      return <ImpresoraCartucho />;
    case "impresora-tanque":
      return <ImpresoraTanque />;
    case "aire-comun":
      return <Aire inverter={false} />;
    case "aire-inverter":
      return <Aire inverter />;
  }
};

// Podio de "concurso": un cilindro con un aro de color
export const Podio: React.FC<{ color: string; alto?: number }> = ({ color, alto = 0.55 }) => (
  <group>
    <mesh position={[0, alto / 2, 0]} castShadow receiveShadow>
      <cylinderGeometry args={[0.5, 0.54, alto, 48]} />
      <Mat c="#eceae4" r={0.6} />
    </mesh>
    <mesh position={[0, alto - 0.07, 0]}>
      <cylinderGeometry args={[0.505, 0.505, 0.05, 48]} />
      <Mat c={color} r={0.4} e={color} ei={0.25} />
    </mesh>
  </group>
);
