# Enigma

A Python implementation of the historical **Enigma machine**, built from scratch as an educational project.

The project simulates the electrical signal path of an Enigma machine, including rotors, reflector, plugboard, and rotor stepping. The same configuration can be used to both encrypt and decrypt messages.

> **Note:** Enigma is a historical cipher and is **not secure by modern cryptographic standards**. This project is intended for educational purposes.

## Features

* Configurable Enigma rotors
* Forward and reverse rotor signal mapping
* Reflector
* Plugboard
* Rotor positions / message key
* Rotor stepping
* Rotor turnover
* Support for multiple rotor configurations
* Encryption and decryption using the same machine configuration
* Command-line interface

## Installation

Clone the repository and install it with `pip`:

```bash
git clone https://github.com/Pietrut/Enigma-Device.git
cd <repository-directory>
pip install -e .
```

After installation, the `enigma` command will be available from your terminal.

## Usage

A basic command looks like:

```bash
enigma --text "TARGET HIT!" --rotors "V-I-II" --plugboard "A-N;T-P;E-H" --message_key "ZKN"
```

For example:

```text
Input:
TARGET HIT!

Output:
BEXYPI ALD!
```

Running the encrypted text through an Enigma machine configured with the **same settings** produces the original message:

```text
BEXYPI ALD!
    ↓
TARGET HIT!
```

### Arguments

| Argument        | Description                                |
| --------------- | ------------------------------------------ |
| `--text`        | Text to encrypt or decrypt                 |
| `--rotors`      | Rotors used by the machine and their order |
| `--plugboard`   | Plugboard connections                      |
| `--message_key` | Initial rotor positions                    |

### Rotor configuration

Rotors are specified using Roman numerals separated by `-`.

For example:

```text
V-I-II
```

Selects rotors V, I, and II in the specified order.

### Plugboard configuration

Plugboard connections are specified as pairs separated by `;`:

```text
A-N;T-P;E-H
```

This connects:

```text
A ↔ N
T ↔ P
E ↔ H
```

Letters that are not connected to another letter pass through unchanged.

## How It Works

The Enigma machine encrypts a letter by passing an electrical signal through several components.

```text
                   Plugboard 
                       ↓
                     Rotor 1
                       ↓
                     Rotor 2
                       ↓
                     Rotor 3
                       ↓
                   Reflector
                       ↓
                     Rotor 3
                       ↓
                     Rotor 2
                       ↓
                     Rotor 1
                       ↓
                   Plugboard 
                       ↓
                     Output
```

Before processing each letter, the rotors step according to their configured positions and turnover points.

The signal then travels through the rotors, reaches the reflector, and travels back through the rotors in the opposite direction.

Because the Enigma's electrical mapping is reciprocal, encrypting an encrypted message with the same configuration returns the original message.

## Historical Configuration

The project uses the standard wiring of historical Enigma rotors and reflector configurations.

The available rotors include:

| Rotor | Wiring                       | Turnover |
| ----- | ---------------------------- | -------- |
| I     | `EKMFLGDQVZNTOWYHXUSPAIBRCJ` | Q        |
| II    | `AJDKSIRUXBLHWTMCQGZNPYFVOE` | E        |
| III   | `BDFHJLCPRTXVZNYEIWGAKMUSQO` | V        |
| IV    | `ESOVPZJAYQUIRHXLNFTGKDCMWB` | J        |
| V     | `VZBRGITYUPSDNHLXAWMJQOFECK` | Z        |

The default reflector is **Reflector B**:

```text
YRUHQSLDPXNGOKMIEBFZCWVJAT
```

## Limitations

This project aims to simulate the core behavior of the Enigma machine, but it should not be considered a replacement for a historically exact reproduction.

Enigma was also fundamentally different from modern cryptographic systems and is not suitable for protecting real-world data.

## License

This project is licensed under the MIT License.
