#!/usr/bin/env python
# -*- coding: utf-8 -*-

import agent_based

agent_based.read("Age-distribution of cases - data.csv", "Age-distribution of cases - model.csv", "Weekly cases - data.csv", "Weekly cases - model.csv", "S - model.csv", "I - model.csv", "R - model.csv")

agent_based.plot("output.pdf")