// SPDX-License-Identifier: MIT

// 0x14DD0E4DE24d5b2dAddf1D472bC2bA2aC75f7D58

pragma solidity 0.8.24;

contract Saludo {

    string saludo = "Saludo incial desde REMIX";

    function leerSaludo() public view returns (string memory) {
        return saludo;
    }

    function guardarSaludo(string memory _nuevoSaludo) public {
        saludo = _nuevoSaludo;
    }

}