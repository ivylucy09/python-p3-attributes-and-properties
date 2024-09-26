#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    
    def __init__(self, name="", job=""):
        self._name = None
        self._job = None
        self.name = name
        self.job = job

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be string between 1 and 25 characters.")
            return
        self._name = name.title()

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, job):
        if job not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
            return
        self._job = job
