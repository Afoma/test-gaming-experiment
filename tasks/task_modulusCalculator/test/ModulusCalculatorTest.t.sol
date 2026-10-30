// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import {Test} from "forge-std/Test.sol";
import {ModulusCalculator} from "../src/ModulusCalculator.sol";

contract ModulusCalculatorTest is Test{

    ModulusCalculator public calc;

    function setUp() external{
        calc = new ModulusCalculator();
    }

    function testModulusCalculator5And3() public{ 
        assertEq(calc.calculateModulus(5,3),2);
    }
}