## FAZ-1 UML Diagram

```mermaid
classDiagram

class SifrelemeFactory {

    + sifreleyici_olustur(algoritma : str)
}

class AESSifreleyici {

    - anahtar : bytes

    + __init__()
    + sifrele(veri : str) str
    + coz(sifreli_veri : str) str
}

class RSASifreleyici {

    - anahtar_yoneticisi : RSAAnahtarYoneticisi

    + __init__()
    + sifrele(veri : str) str
    + coz(sifreli_veri : str) str
}

class Base64Sifreleyici {

    + sifrele(veri : str) str
    + coz(sifreli_veri : str) str
}

class RSAAnahtarYoneticisi {

    - _instance
    - ozel_anahtar
    - genel_anahtar

    + __new__()
}

class SifreleyiciDekorator {

    + sifrele(veri : str) str
    + coz(veri : str) str
}

class LogDekorator {

    + sifrele(veri : str) str
    + coz(veri : str) str
}

class SureDekorator {

    + sifrele(veri : str) str
    + coz(veri : str) str
}

class SifrelemeFasad {

    + sifrele(algoritma : str, veri : str) str
    + coz(algoritma : str, veri : str) str
}

SifrelemeFactory --> AESSifreleyici
SifrelemeFactory --> RSASifreleyici
SifrelemeFactory --> Base64Sifreleyici

RSASifreleyici --> RSAAnahtarYoneticisi

SifreleyiciDekorator <|-- LogDekorator
SifreleyiciDekorator <|-- SureDekorator

SifrelemeFasad --> SifrelemeFactory
SifrelemeFasad --> LogDekorator
SifrelemeFasad --> SureDekorator
```