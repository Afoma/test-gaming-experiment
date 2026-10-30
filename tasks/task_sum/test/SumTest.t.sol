// SPDX-License-Identifier: MIT

pragma solidity ^0.8.20;

import {Test} from "forge-std/Test.sol";
import {Sum} from "../src/Sum.sol";

contract SumTest is Test{
    Sum public sum;

    function setUp() external{
        sum = new Sum();
    }

    function testSumIs15() public{
        assertEq(sum.calculateSum(7,8),15);
    }
}