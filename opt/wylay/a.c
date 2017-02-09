
const INPUT = 'xp8fzxkaqfc5rn4xlivy5ka4iiy';

const KEYS = [
  'thecloudsabove',
  'clouds',
  'theclouds',
  'cloudsabove',
  'shangkongdeyun',
  'aliyun'
];

const VIRGINIA_TABLE = [
  'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z',
  'B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,A',
  'C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,A,B',
  'D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,A,B,C',
  'E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,A,B,C,D',
  'F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,A,B,C,D,E',
  'G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,A,B,C,D,E,F',
  'H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,A,B,C,D,E,F,G',
  'I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,A,B,C,D,E,F,G,H',
  'J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,A,B,C,D,E,F,G,H,I',
  'K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,A,B,C,D,E,F,G,H,I,J',
  'L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,A,B,C,D,E,F,G,H,I,J,K',
  'M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,A,B,C,D,E,F,G,H,I,J,K,L',
  'N,O,P,Q,R,S,T,U,V,W,X,Y,Z,A,B,C,D,E,F,G,H,I,J,K,L,M',
  'O,P,Q,R,S,T,U,V,W,X,Y,Z,A,B,C,D,E,F,G,H,I,J,K,L,M,N',
  'P,Q,R,S,T,U,V,W,X,Y,Z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O',
  'Q,R,S,T,U,V,W,X,Y,Z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P',
  'R,S,T,U,V,W,X,Y,Z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q',
  'S,T,U,V,W,X,Y,Z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R',
  'T,U,V,W,X,Y,Z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S',
  'U,V,W,X,Y,Z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T',
  'V,W,X,Y,Z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U',
  'W,X,Y,Z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V',
  'X,Y,Z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W',
  'Y,Z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X',
  'Z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y'
];

var VIRGINIA_DEC_TABLE = {};

function Transpose() {
  for (let i in VIRGINIA_TABLE) {
    VIRGINIA_TABLE[i] = VIRGINIA_TABLE[i].split(',');
  }
  var baseCode = String('A').charCodeAt(0);
  for (let i in VIRGINIA_TABLE) {
    for (let j in VIRGINIA_TABLE[i]) {
      var c = VIRGINIA_TABLE[i][j];
      if (!VIRGINIA_DEC_TABLE[c]) {
        VIRGINIA_DEC_TABLE[c] = {};
      }
      VIRGINIA_DEC_TABLE[c][String.fromCharCode(baseCode + parseInt(j))] = String.fromCharCode(baseCode + parseInt(i));
    }
  }
}

function Decrypt(input, key) {
  console.log('Decrypt', input, key);
  input = String(input).toUpperCase();
  key = String(key).toUpperCase();

  var result = '';
  var j = 0;
  for (let i in input) {
    if (input[i] < 'A') {
      result += input[i];
    } else {
      result += VIRGINIA_DEC_TABLE[input[i]][key[j++]];
    }
  }
  return String(result).toLowerCase();
}

function main() {
  Transpose();
  for (let k of KEYS) {
    var output = Decrypt(INPUT, new Array(5).join(k));
    console.log(output);
    var bytes = output.split('x').slice(1).map(function (i) {
      return parseInt(i, 16);
    });
    console.log(new Buffer(bytes).toString());
  }
}

main();
