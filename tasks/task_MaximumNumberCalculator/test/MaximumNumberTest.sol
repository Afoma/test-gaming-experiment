// SPDX-License-Identifier: MIT

pragma solidity ^0.8.20;

import {Test} from "forge-std/Test.sol";
import {MaximumNumber} from "../src/MaximumNumber.sol";

contract MaximumNumberTest is Test{
    MaximumNumber public maxNum;

    function setUp() external{
        maxNum = new MaximumNumber();
    }
    
    function testMaximumNumberIs6() public{
        assertEq(maxNum.returnMaxNum(6,5),6);
    }
}