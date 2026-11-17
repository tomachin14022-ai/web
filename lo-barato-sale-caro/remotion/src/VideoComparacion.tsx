import { Audio } from "@remotion/media";
import { loadFont } from "@remotion/fonts";
import { ThreeCanvas } from "@remotion/three";
import React from "react";
import { AbsoluteFill, Easing, interpolate, staticFile, useCurrentFrame, useVideoConfig } from "remotion";
import { Camara, Escenario, proyectar, type Toma, type Vec3 } from "./3d/Escenario";
import { Personaje } from "./3d/Personaje";
import { Podio, Producto, type TipoProducto } from "./3d/Productos";
import { Torre } from "./3d/Torre";
import { pesos, total, VIDEOS } from "./datos/videos";

// Fuentes locales (public/fuentes, licencia OFL): el render no depende de internet
const ANTON = "Anton";
const INTER = "Inter";
loadFont({ family: ANTON, url: staticFile("fuentes/anton-latin.woff2"), weight: "400" });
loadFont({ family: INTER, url: staticFile("fuentes/inter-latin.woff2"), weight: "100 900" });

const AMARILLO = "#ffcc00";
const ROJO = "#ff3b30";
const BLANCO = "#fbf8f1";
const TINTA = "#121216";

// Zona segura común a Reels, TikTok y Shorts: el texto importante va en x 120–888, y 288–1248
const SEG_X = 120;
const SEG_ANCHO = 768;

const XA = -0.85;
const XB = 0.85;
const ZP = -0.3;
const ALTO_PODIO = 0.55;
const ALTO_TORRE_MAX = 2.6;

const ESCALA: Record<TipoProducto, number> = {
  "cafetera-capsulas": 1.45,
  "cafetera-espresso": 1.25,
  "impresora-cartucho": 1.15,
  "impresora-tanque": 1.1,
  "aire-comun": 0.92,
  "aire-inverter": 0.92,
};
const ALTO_PRODUCTO: Record<TipoProducto, number> = {
  "cafetera-capsulas": 0.56,
  "cafetera-espresso": 0.62,
  "impresora-cartucho": 0.5,
  "impresora-tanque": 0.52,
  "aire-comun": 0.3,
  "aire-inverter": 0.3,
};

const clamp = { extrapolateLeft: "clamp", extrapolateRight: "clamp" } as const;
const SALIDA = Easing.bezier(0.16, 1, 0.3, 1);
const SUAVE = Easing.inOut(Easing.cubic);

const mezclar = (a: Toma, b: Toma, k: number): Toma => ({
  pos: a.pos.map((v, i) => v + (b.pos[i] - v) * k) as Vec3,
  mira: a.mira.map((v, i) => v + (b.mira[i] - v) * k) as Vec3,
  fov: a.fov + (b.fov - a.fov) * k,
});

// Texto grande estilo miniatura: Anton, blanco con una palabra en color y sombra dura
const Titulo: React.FC<{ lineas: { texto: string; color?: string; tam?: number }[]; top: number; tam: number; k: number; salida?: number }> = ({
  lineas,
  top,
  tam,
  k,
  salida = 0,
}) => (
  <div
    style={{
      position: "absolute",
      left: SEG_X,
      width: SEG_ANCHO,
      top,
      textAlign: "center",
      fontFamily: ANTON,
      fontSize: tam,
      lineHeight: 1.02,
      letterSpacing: 1,
      opacity: Math.min(k, 1 - salida),
      scale: String(0.92 + 0.08 * k),
      translate: `0px ${(1 - k) * 30 - salida * 30}px`,
      textShadow: "0 7px 0 rgba(0,0,0,0.45), 0 0 30px rgba(0,0,0,0.35)",
    }}
  >
    {lineas.map((l) => (
      <div key={l.texto} style={{ color: l.color ?? BLANCO, fontSize: l.tam ?? tam, textWrap: "balance" }}>
        {l.texto}
      </div>
    ))}
  </div>
);

// Cartel anclado a un punto de la escena 3D
const Cartel: React.FC<{ x: number; y: number; k: number; children: React.ReactNode; fondo?: string; minY?: number }> = ({
  x,
  y,
  k,
  children,
  fondo = BLANCO,
  minY = 0,
}) => {
  const cx = Math.min(Math.max(x, SEG_X + 150), SEG_X + SEG_ANCHO - 150);
  return (
    <div
      style={{
        position: "absolute",
        left: cx,
        top: Math.max(y, minY),
        translate: "-50% -100%",
        scale: String(0.9 + 0.1 * k),
        opacity: k,
        background: fondo,
        color: TINTA,
        borderRadius: 18,
        padding: "10px 22px 12px",
        textAlign: "center",
        boxShadow: "0 10px 0 rgba(0,0,0,0.28)",
        whiteSpace: "nowrap",
      }}
    >
      {children}
    </div>
  );
};

export const VideoComparacion: React.FC<{ video: string }> = ({ video }) => {
  const d = VIDEOS[video];
  const frame = useCurrentFrame();
  const { fps, width, height } = useVideoConfig();
  const T = frame / fps;
  const t = d.t;
  const p = (desde: number, dur = 0.45, easing = SALIDA) => interpolate(T, [desde, desde + dur], [0, 1], { ...clamp, easing });

  // ---------- Cámara ----------
  const ancho = (z: number): Toma => ({ pos: [0, 1.75, z], mira: [0, 1.08, 0], fov: 34 });
  const tope = (tipo: TipoProducto) => ALTO_PODIO + ALTO_PRODUCTO[tipo] * ESCALA[tipo];
  const cerca = (x: number, tipo: TipoProducto): Toma => ({
    pos: [x * 0.92, tope(tipo) + 0.42, 3.5],
    mira: [x, tope(tipo) - 0.03, ZP],
    fov: 31,
  });
  const torres: Toma = { pos: [0, 1.95, 8.6], mira: [0, 1.4, -0.3], fov: 36 };
  const alto: Toma = { pos: [0, 2.45, 11.2], mira: [0, 2.15, -0.3], fov: 38 };
  let toma = mezclar(ancho(8.4), ancho(7.5), interpolate(T, [0, t.a], [0, 1], clamp));
  toma = mezclar(toma, cerca(XA, d.a.tipo), p(t.a - 0.2, 0.6, SUAVE));
  toma = mezclar(toma, cerca(XB, d.b.tipo), p(t.b - 0.2, 0.6, SUAVE));
  toma = mezclar(toma, torres, p(t.uso - 0.15, 0.7, SUAVE));
  toma = mezclar(toma, alto, p(t.gana - 0.1, 1.2, SUAVE));
  // Pulso de cámara en mano (siempre hay algo moviéndose)
  toma = {
    ...toma,
    pos: [toma.pos[0] + Math.sin(T * 0.9) * 0.03, toma.pos[1] + Math.sin(T * 1.3) * 0.02, toma.pos[2]],
  };
  const aPantalla = (pt: Vec3) => proyectar(pt, toma, width, height);

  // ---------- Torres de plata (costo acumulado) ----------
  const k = ALTO_TORRE_MAX / Math.max(total(d.a, d.usoMes, d.meses), total(d.b, d.usoMes, d.meses));
  const crece = p(t.uso + 0.1, 0.6);
  const mes =
    T < t.cruce
      ? interpolate(T, [t.uso + 0.6, t.cruce], [0, d.cruceMes], { ...clamp, easing: Easing.inOut(Easing.quad) })
      : interpolate(T, [t.gana, t.ahorro - 0.1], [d.cruceMes, d.meses], { ...clamp, easing: Easing.in(Easing.quad) });
  const mesEntero = Math.floor(mes);
  const hA = total(d.a, d.usoMes, mes) * k * crece;
  const hB = total(d.b, d.usoMes, mes) * k * crece;
  const fueraProducto = p(t.uso - 0.1, 0.35, Easing.in(Easing.back(1.6)));

  // ---------- Personaje ----------
  const parpadeo = [1.2, 3.9, 6.8, 9.6, 12.2, 14.4, 17.1, 19.9, 22.3].reduce(
    (m, b) => Math.max(m, interpolate(T, [b, b + 0.06, b + 0.14], [0, 1, 0], clamp)),
    0,
  );
  const tramos = (puntos: [number, number][]) =>
    interpolate(
      T,
      puntos.map((q) => q[0]),
      puntos.map((q) => q[1]),
      { ...clamp, easing: SUAVE },
    );
  const pq = t.pregunta;
  const cabezaGiro = tramos([
    [0, -0.45],
    [1.45, -0.45],
    [1.75, 0],
    [pq, 0],
    [pq + 0.3, -0.55],
    [pq + 1.0, -0.55],
    [pq + 1.3, 0.55],
    [pq + 2.1, 0.55],
    [pq + 2.4, 0],
    [t.a - 0.1, 0],
    [t.a + 0.3, -0.45],
    [t.b - 0.1, -0.45],
    [t.b + 0.3, 0.45],
    [t.uso - 0.1, 0.45],
    [t.uso + 0.3, -0.25],
    [t.gana, -0.25],
    [t.gana + 0.3, 0.35],
    [t.link, 0.35],
    [t.link + 0.3, 0],
  ]);
  const giro = tramos([
    [t.a - 0.1, 0],
    [t.a + 0.3, -0.3],
    [t.b - 0.1, -0.3],
    [t.b + 0.3, 0.3],
    [t.uso, 0.3],
    [t.uso + 0.3, 0],
    [t.gana, 0],
    [t.gana + 0.3, 0.35],
    [t.ahorro, 0.35],
    [t.ahorro + 0.3, 0],
  ]);
  const cabezaArriba = tramos([
    [t.uso, 0],
    [t.uso + 0.4, 0.3],
    [t.link, 0.3],
    [t.link + 0.3, 0],
  ]);
  const cejas = tramos([
    [0, -0.85],
    [1.55, -0.85],
    [1.75, 1],
    [pq - 0.1, 1],
    [pq + 0.2, 0.5],
    [t.a, 0.5],
    [t.a + 0.2, -0.7],
    [t.b, -0.7],
    [t.b + 0.2, 0.4],
    [t.uso, 0.4],
    [t.uso + 0.2, 1],
    [t.gana, 1],
    [t.gana + 0.2, 0.2],
  ]);
  const brazoDer = tramos([
    [t.gana, 0],
    [t.gana + 0.3, 1.05],
    [t.ahorro, 1.05],
    [t.ahorro + 0.3, 1.55],
    [t.link - 0.1, 1.55],
    [t.link + 0.2, 1.65],
  ]) + (T > t.link ? Math.sin((T - t.link) * 11) * 0.12 : 0);
  const brazoIzq = tramos([
    [t.ahorro, 0],
    [t.ahorro + 0.3, 1.55],
    [t.link - 0.1, 1.55],
    [t.link + 0.2, 0],
  ]);
  const salto =
    Math.max(0, Math.sin(Math.min(1, Math.max(0, (T - 1.72) / 0.35)) * Math.PI)) * 0.12 +
    Math.max(0, Math.sin(Math.min(1, Math.max(0, (T - t.vuelta) / 0.35)) * Math.PI)) * 0.14 +
    Math.max(0, Math.sin(Math.min(1, Math.max(0, (T - t.numAhorro) / 0.4)) * Math.PI)) * 0.18;

  // ---------- Textos ----------
  const titulo = (() => {
    if (T < t.pregunta - 0.05) {
      return (
        <Titulo
          top={300}
          tam={88}
          k={1}
          lineas={[{ texto: d.gancho[0] }, { texto: d.gancho[1] }, { texto: d.gancho[2], color: AMARILLO, tam: 128 }]}
        />
      );
    }
    if (T < t.a - 0.05) return <Titulo top={330} tam={116} k={p(t.pregunta)} lineas={[{ texto: "¿CUÁL COMPRÁS?", color: AMARILLO }]} />;
    if (T < t.b - 0.05) return <Titulo top={330} tam={96} k={p(t.a)} lineas={[{ texto: d.tituloA }]} />;
    if (T < t.uso - 0.05) return <Titulo top={330} tam={96} k={p(t.b)} lineas={[{ texto: d.tituloB }]} />;
    if (T < t.vuelta) {
      return (
        <>
          <Titulo top={300} tam={66} k={p(t.uso)} lineas={[{ texto: d.tituloUso }]} />
          <Titulo top={450} tam={140} k={p(t.uso + 0.4)} lineas={[{ texto: `MES ${mesEntero}`, color: AMARILLO }]} />
        </>
      );
    }
    if (T < t.gana - 0.05) {
      return (
        <>
          <Titulo top={310} tam={78} k={1} lineas={[{ texto: `MES ${mesEntero}` }]} />
          <Titulo top={410} tam={150} k={p(t.vuelta, 0.25, Easing.out(Easing.back(2.2)))} lineas={[{ texto: "SE DA VUELTA", color: AMARILLO }]} />
        </>
      );
    }
    if (T < t.ahorro - 0.05) {
      return (
        <>
          <Titulo top={310} tam={78} k={1} lineas={[{ texto: `MES ${mesEntero}` }]} />
          <Titulo top={410} tam={120} k={p(t.gana)} lineas={[{ texto: "DESDE AHÍ" }, { texto: d.gana, color: AMARILLO }]} />
        </>
      );
    }
    if (T < t.link - 0.05) {
      const cuenta = interpolate(T, [t.numAhorro - 0.7, t.numAhorro], [0, total(d.a, d.usoMes, d.meses) - total(d.b, d.usoMes, d.meses)], {
        ...clamp,
        easing: Easing.out(Easing.cubic),
      });
      return (
        <>
          <Titulo top={310} tam={92} k={p(t.ahorro)} lineas={[{ texto: `EN ${d.anios} AÑOS AHORRÁS` }]} />
          <Titulo top={420} tam={150} k={p(t.numAhorro - 0.7)} lineas={[{ texto: pesos(cuenta), color: AMARILLO }]} />
        </>
      );
    }
    return <Titulo top={340} tam={150} k={p(t.link, 0.3, Easing.out(Easing.back(2)))} lineas={[{ texto: "LINK" }, { texto: "EN LA BIO", color: AMARILLO }]} />;
  })();

  // Carteles anclados a los productos y a las torres
  const sobre = (x: number, alto: number) => aPantalla([x, alto, ZP]);
  const topeA = ALTO_PODIO + ALTO_PRODUCTO[d.a.tipo] * ESCALA[d.a.tipo] + 0.12;
  const topeB = ALTO_PODIO + ALTO_PRODUCTO[d.b.tipo] * ESCALA[d.b.tipo] + 0.12;
  const precioK = (desde: number) => p(desde, 0.3, Easing.out(Easing.back(2))) * (1 - p(t.a - 0.15, 0.2));
  const cartelPrecio = (x: number, tope: number, precio: number, corto: string, desde: number) => {
    const q = sobre(x, tope);
    return (
      <Cartel x={q.x} y={q.y} k={precioK(desde)}>
        <div style={{ fontFamily: INTER, fontWeight: 900, fontSize: 26, letterSpacing: 2, opacity: 0.6 }}>{corto}</div>
        <div style={{ fontFamily: ANTON, fontSize: 64, lineHeight: 1.05 }}>{pesos(precio)}</div>
      </Cartel>
    );
  };
  const costoUso = (valor: string, color: string, desde: number, hasta: number) => {
    const kk = p(desde, 0.3, Easing.out(Easing.back(2.2))) * (1 - p(hasta, 0.2));
    return (
      <Cartel x={SEG_X + SEG_ANCHO / 2} y={770} k={kk} fondo={color}>
        <div style={{ fontFamily: ANTON, fontSize: 120, lineHeight: 1 }}>{valor}</div>
        <div style={{ fontFamily: INTER, fontWeight: 900, fontSize: 30, letterSpacing: 2 }}>{d.unidad}</div>
      </Cartel>
    );
  };
  const ratioK = p(t.ratio, 0.3, Easing.out(Easing.back(2.5))) * (1 - p(t.uso - 0.15, 0.2));
  const cartelTorre = (x: number, h: number, o: { precio: number; porUso: number }, color: string, retraso: number) => {
    const q = aPantalla([x, ALTO_PODIO + h + 0.12, ZP]);
    const kk = p(t.uso + 0.5 + retraso, 0.3);
    return (
      <Cartel x={q.x} y={q.y} k={kk} fondo={color} minY={690}>
        <div style={{ fontFamily: ANTON, fontSize: 52, lineHeight: 1.05 }}>{pesos(total(o, d.usoMes, mes))}</div>
      </Cartel>
    );
  };

  // Subtítulo: una palabra por vez, como en las referencias
  const palabra = d.palabras.find((w, i) => T >= w.desde && T < (d.palabras[i + 1]?.desde ?? w.hasta + 0.4));
  const popPalabra = palabra ? interpolate(T, [palabra.desde, palabra.desde + 0.09], [0.86, 1], clamp) : 1;
  const flash =
    interpolate(T, [t.vuelta - 0.01, t.vuelta, t.vuelta + 0.28], [0, 0.4, 0], clamp) +
    interpolate(T, [t.numAhorro - 0.01, t.numAhorro, t.numAhorro + 0.25], [0, 0.25, 0], clamp);

  return (
    <AbsoluteFill style={{ backgroundColor: d.colores.pared }}>
      <Audio src={staticFile(d.audio)} />
      <ThreeCanvas width={width} height={height} shadows>
        <Camara {...toma} />
        <Escenario frame={frame} pared={d.colores.pared} piso={d.colores.piso} contraluz={d.colores.contraluz} />
        {/* Barata (izquierda) y cara (derecha) */}
        <group position={[XA, 0, ZP]}>
          <Podio color={ROJO} />
          <group position={[0, ALTO_PODIO, 0]} scale={ESCALA[d.a.tipo] * (1 - fueraProducto)}>
            <Producto tipo={d.a.tipo} />
          </group>
          {crece > 0 ? (
            <group position={[0, ALTO_PODIO, 0]}>
              <Torre alto={hA} color="#7cc47a" />
            </group>
          ) : null}
        </group>
        <group position={[XB, 0, ZP]}>
          <Podio color={AMARILLO} />
          <group position={[0, ALTO_PODIO, 0]} scale={ESCALA[d.b.tipo] * (1 - fueraProducto)}>
            <Producto tipo={d.b.tipo} />
          </group>
          {crece > 0 ? (
            <group position={[0, ALTO_PODIO, 0]}>
              <Torre alto={hB} color="#7cc47a" />
            </group>
          ) : null}
        </group>
        <Personaje
          z={0.75}
          giro={giro}
          cabezaGiro={cabezaGiro}
          cabezaArriba={cabezaArriba}
          cejas={cejas}
          parpadeo={parpadeo}
          brazoDer={brazoDer}
          brazoIzq={brazoIzq}
          respira={T * 2.4}
          salto={salto}
        />
      </ThreeCanvas>

      {/* Viñeta suave */}
      <AbsoluteFill style={{ background: "radial-gradient(ellipse at 50% 45%, rgba(0,0,0,0) 55%, rgba(0,0,0,0.45) 100%)" }} />

      {cartelPrecio(XA, topeA, d.a.precio, d.a.corto, t.pregunta + 0.1)}
      {cartelPrecio(XB, topeB, d.b.precio, d.b.corto, t.pregunta + 0.25)}
      {costoUso(d.porUsoA, ROJO, t.numA - 0.05, t.b - 0.15)}
      {costoUso(d.porUsoB, AMARILLO, t.numB - 0.05, t.uso - 0.15)}
      <div
        style={{
          position: "absolute",
          left: SEG_X,
          width: SEG_ANCHO,
          top: 800,
          textAlign: "center",
          opacity: ratioK,
          scale: String(0.85 + 0.15 * ratioK),
          rotate: "-3deg",
        }}
      >
        <span
          style={{
            display: "inline-block",
            fontFamily: ANTON,
            fontSize: 84,
            color: TINTA,
            background: AMARILLO,
            padding: "4px 28px 8px",
            borderRadius: 14,
            boxShadow: "0 9px 0 rgba(0,0,0,0.3)",
          }}
        >
          {d.ratio}
        </span>
      </div>
      {crece > 0.01 && T < t.link - 0.05 ? (
        <>
          {cartelTorre(XA, hA, d.a, ROJO, 0)}
          {cartelTorre(XB, hB, d.b, BLANCO, 0.1)}
        </>
      ) : null}

      {titulo}

      {palabra ? (
        <div
          style={{
            position: "absolute",
            left: SEG_X,
            width: SEG_ANCHO,
            top: 1150,
            textAlign: "center",
            fontFamily: INTER,
            fontWeight: 900,
            fontSize: 62,
            color: BLANCO,
            WebkitTextStroke: "12px #121216",
            paintOrder: "stroke fill",
            scale: String(popPalabra),
          }}
        >
          {palabra.texto.replace(/[.,]$/, "").toLowerCase()}
        </div>
      ) : null}

      <AbsoluteFill style={{ backgroundColor: "#ffffff", opacity: flash }} />
    </AbsoluteFill>
  );
};
