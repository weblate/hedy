// This file was generated by lezer-generator. You probably shouldn't edit it.
// (It was then subsequently modified by generate-lezer-parsers).
import {LRParser} from "@lezer/lr"
import {specializeKeywordGen, extendKeywordGen} from "./tokens"
export function generateParser(level: number, language: string): LRParser {
  const specializeKeyword = specializeKeywordGen(level, language);
  const extendKeyword = extendKeywordGen(level, language);
  return LRParser.deserialize({
  version: 14,
  states: "'OQ]QPOOOOQO'#Ct'#CtQ]QPOOOwQPO'#CwO!VQPO'#CsOOQO'#Cy'#CyO!bQPO'#ClOOQO'#Cz'#CzO!jQPO'#CmOOQO'#C{'#C{O!rQPO'#CoOOQO'#C|'#C|O!zQPO'#CpOOQO'#C}'#C}O#SQPO'#CqOOQO'#Cn'#CnOOQO'#DO'#DOO#[QPO'#CrOOQO'#Ch'#ChQrQPO'#CuQ#jQPOOOOQO-E6r-E6rOOQO'#Cv'#CvO$RQPO,59TOOQO'#Cw'#CwOOQO-E6u-E6uO$^QPO,59WOOQO-E6w-E6wO$iQPO,59XOOQO-E6x-E6xOOQO-E6y-E6yOOQO,59Z,59ZOOQO-E6z-E6zOOQO,59[,59[OOQO-E6{-E6{OOQO,59],59]O$tQPO,59^OOQO-E6|-E6|O%PQPO,59aOOQO-E6s-E6sOOQO-E6t-E6tO%nQPO1G.oOOQO'#Cx'#CxO%yQPO1G.qO&RQPO7+$]OOQO-E6v-E6v",
  stateData: "&^~OXOSuOSYOS~OQTORXOSZOT]OU`OVVO^ROvPO~OWfO^kXskXvkX~O^hOsgXvgX~OQTO^hO~OVVO^hO~ORXO^oO~OSZO^qO~OT]O^sO~OU`O^hOsfXvfX~OQTORXOSZOT]OU`OVVO^RO~OPzOWfO^hO~O^hOs`av`a~O^hOsaavaa~O^hOsfavfa~OvPOQiaRiaSiaTiaUiaVia^iasia~O^hOs]iv]i~OPzO^hO~O^hOs_qv_q~O",
  goto: "$bsPPPPPPPPPPPPtyPyyyy!O!O!Oyy!T!_!f!l#Y#`#h#p#x$Q$YVcOQdVbOQdV_OQdQQOSeQvRvcSdOQRwdQgRRxgUSOQd[iSjlty|QjUQlWQtaQygR|{Q{gR}{UUOQdRkUUWOQdRmWUYOQdRnYU[OQdRp[U^OQdRr^UaOQdRua",
  nodeNames: "⚠ ask print forward turn color sleep play is Comment SpecialChar Program Command Assign Text Ask Print Play Turtle Forward Turn Color Sleep ErrorInvalid",
  maxTerm: 38,
  nodeProps: [
    ["group", 18,"turtle"]
  ],
  skippedNodes: [0,9,10],
  repeatNodeCount: 11,
  tokenData: "#j~R^OY}YZ!rZp}pq!wqr!|rs}st#Rt!O}!O!P!|!P!a}!a!b!|!b;'S};'S;=`!l<%lO}~!SW^~OY}Zp}rs}t!O}!P!a}!b;'S};'S;=`!l<%lO}~!oP;=`<%l}~!wOv~~!|Ou~~#ROY~~#WSX~OY#RZ;'S#R;'S;=`#d<%lO#R~#gP;=`<%l#R",
  tokenizers: [0],
  topRules: {"Program":[0,11]},
  dynamicPrecedences: {"23":-10},
  specialized: [{term: 14, get: (value: any, stack: any) => (specializeKeyword(value, stack) << 1), external: specializeKeyword},{term: 14, get: (value: any, stack: any) => (extendKeyword(value, stack) << 1) | 1, external: extendKeyword, extend: true}],
  tokenPrec: 0
})
}
