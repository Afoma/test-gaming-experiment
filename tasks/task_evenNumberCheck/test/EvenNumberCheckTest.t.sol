// SPDX-License-Identifier: MIT

pragma solidity ^0.8.20;

import {Test} from "../lib/forge-std/src/Test.sol";
import {EvenNumberCheck} from "../src/EvenNumberCheck.sol";

contract EvenNumberCheckTest is Test{
    EvenNumberCheck public checkEvenNum;

    function setUp() external{
        checkEvenNum = new EvenNumberCheck();
    }

    function testCheckEvenNumberReturnsTrue() public{
        assertTrue(checkEvenNum.checkEvenNumber(20));
    }
}