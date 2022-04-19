#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy


def add(a, b):
    return a + b


def main():
    pass


if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
