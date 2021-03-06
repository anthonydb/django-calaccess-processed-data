#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Load the OCD Election model with data from the scraped CandidateElection model.
"""
from calaccess_processed.models import (
    ScrapedIncumbentElectionProxy,
    ScrapedCandidateElectionProxy,
)
from calaccess_processed.management.commands import LoadOCDElectionsBase


class Command(LoadOCDElectionsBase):
    """
    Load the OCD Election model with data from the scraped CandidateElection model.
    """
    help = 'Load the OCD Election model with data from the scraped CandidateElection model'

    def handle(self, *args, **options):
        """
        Make it happen.
        """
        super(Command, self).handle(*args, **options)
        self.header("Loading Election from scraped incumbents")
        self.load_from_proxy(ScrapedIncumbentElectionProxy)
        self.header("Loading Election from scraped candidates")
        self.load_from_proxy(ScrapedCandidateElectionProxy)
        self.success("Done!")
