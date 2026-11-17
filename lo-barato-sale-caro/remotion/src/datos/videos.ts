import type { TipoProducto } from "../3d/Productos";
import palabrasAire from "./palabras-aire.json";
import palabrasCafetera from "./palabras-cafetera.json";
import palabrasImpresora from "./palabras-impresora.json";

export type Palabra = { texto: string; desde: number; hasta: number };

// Momentos clave en segundos, tomados de los tiempos por palabra de la voz
export type Tiempos = {
  pregunta: number; // "¿Cuál comprás?"
  a: number; // empieza a hablar de la barata
  numA: number; // dice el costo por uso de la barata
  b: number; // empieza a hablar de la cara
  numB: number;
  ratio: number; // "x veces menos"
  uso: number; // "Si tomás…"
  cruce: number; // dice el número del mes
  vuelta: number; // "se da vuelta"
  gana: number; // "Desde ahí gana la cara"
  ahorro: number; // "En 3 años…"
  numAhorro: number;
  link: number; // "Link en la bio"
  fin: number; // duración total del video
};

export type DatosVideo = {
  id: string;
  audio: string;
  a: { tipo: TipoProducto; corto: string; precio: number; porUso: number };
  b: { tipo: TipoProducto; corto: string; precio: number; porUso: number };
  usoMes: number;
  meses: number;
  cruceMes: number;
  gancho: [string, string, string];
  tituloA: string;
  tituloB: string;
  unidad: string; // "POR CAFÉ"
  porUsoA: string;
  porUsoB: string;
  ratio: string;
  tituloUso: string;
  gana: string;
  anios: number;
  colores: { pared: string; piso: string; contraluz: string };
  palabras: Palabra[];
  t: Tiempos;
};

// Datos de los videos anteriores (precios de Mercado Libre del 17/11/26)
export const VIDEOS: Record<string, DatosVideo> = {
  cafetera: {
    id: "cafetera",
    audio: "voz/cafetera.mp3",
    a: { tipo: "cafetera-capsulas", corto: "CÁPSULAS", precio: 174400, porUso: 2400 },
    b: { tipo: "cafetera-espresso", corto: "ESPRESSO", precio: 850000, porUso: 78000 / 111 },
    usoMes: 60,
    meses: 36,
    cruceMes: 7,
    gancho: ["LA CAFETERA BARATA", "TE SALE", "MÁS DEL DOBLE"],
    tituloA: "CON CÁPSULAS",
    tituloB: "CON CAFÉ EN GRANO",
    unidad: "POR CAFÉ",
    porUsoA: "$2.400",
    porUsoB: "$703",
    ratio: "3 VECES MENOS",
    tituloUso: "SI TOMÁS 2 CAFÉS POR DÍA",
    gana: "GANA LA CARA",
    anios: 3,
    colores: { pared: "#2a1c18", piso: "#4a3127", contraluz: "#ff9a52" },
    palabras: palabrasCafetera,
    t: {
      pregunta: 2.5,
      a: 5.5,
      numA: 6.51,
      b: 8.4,
      numB: 9.71,
      ratio: 11.09,
      uso: 12.6,
      cruce: 15.27,
      vuelta: 15.34,
      gana: 16.45,
      ahorro: 18.25,
      numAhorro: 19.5,
      link: 20.9,
      fin: 22.4,
    },
  },
  impresora: {
    id: "impresora",
    audio: "voz/impresora.mp3",
    a: { tipo: "impresora-cartucho", corto: "CARTUCHOS", precio: 430000, porUso: 25700 / 120 },
    b: { tipo: "impresora-tanque", corto: "TANQUE", precio: 668000, porUso: 21700 / 4500 },
    usoMes: 100,
    meses: 36,
    cruceMes: 12,
    gancho: ["LA IMPRESORA BARATA", "TE SALE", "CASI EL DOBLE"],
    tituloA: "CON CARTUCHOS",
    tituloB: "CON TANQUE DE TINTA",
    unidad: "POR HOJA",
    porUsoA: "$214",
    porUsoB: "$4,8",
    ratio: "44 VECES MENOS",
    tituloUso: "SI IMPRIMÍS 100 HOJAS POR MES",
    gana: "GANA LA CARA",
    anios: 3,
    colores: { pared: "#1d2748", piso: "#2a3459", contraluz: "#6f8cff" },
    palabras: palabrasImpresora,
    t: {
      pregunta: 2.35,
      a: 5.0,
      numA: 6.18,
      b: 7.8,
      numB: 9.87,
      ratio: 10.24,
      uso: 12.5,
      cruce: 14.96,
      vuelta: 15.37,
      gana: 16.3,
      ahorro: 18.0,
      numAhorro: 19.47,
      link: 21.0,
      fin: 22.6,
    },
  },
  aire: {
    id: "aire",
    audio: "voz/aire.mp3",
    a: { tipo: "aire-comun", corto: "COMÚN", precio: 973000, porUso: 173.4 },
    b: { tipo: "aire-inverter", corto: "INVERTER", precio: 1087000, porUso: 121.4 },
    usoMes: 100,
    meses: 60,
    cruceMes: 22,
    gancho: ["EL AIRE BARATO", "TE SALE", "MÁS CARO"],
    tituloA: "EL COMÚN",
    tituloB: "EL INVERTER",
    unidad: "POR HORA",
    porUsoA: "$173",
    porUsoB: "$121",
    ratio: "30 % MENOS",
    tituloUso: "8 HORAS POR DÍA, 5 MESES AL AÑO",
    gana: "GANA EL CARO",
    anios: 5,
    colores: { pared: "#123241", piso: "#1d4a5c", contraluz: "#5fd3ff" },
    palabras: palabrasAire,
    t: {
      pregunta: 2.05,
      a: 5.65,
      numA: 6.62,
      b: 8.2,
      numB: 9.59,
      ratio: 10.73,
      uso: 12.45,
      cruce: 15.93,
      vuelta: 16.42,
      gana: 17.33,
      ahorro: 18.93,
      numAhorro: 20.37,
      link: 21.97,
      fin: 23.4,
    },
  },
};

export const total = (o: { precio: number; porUso: number }, uso: number, mes: number) => o.precio + uso * mes * o.porUso;

export const pesos = (n: number) => "$" + Math.round(n).toLocaleString("es-AR");
