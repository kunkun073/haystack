# coding: utf8
"""Custom Errors for Haystack"""

from jsonschema.exceptions import ValidationError


class HaystackError(Exception):
    """Any error generated by Haystack"""

    pass


class DocumentStoreError(HaystackError):
    """Exception for issues that occur in a document store"""

    pass


class DuplicateDocumentError(DocumentStoreError, ValueError):
    """Exception for Duplicate document"""

    pass


class PipelineError(HaystackError):
    """Exception for issues raised within a pipeline"""

    pass


class PipelineValidationError(PipelineError):
    """ 
    Exception for issues that occur while loading a pipeline 
    
    `PipelineValidationError` is quite informative, as it 
    wraps a `jsonschema.exceptions.ValidationError`. 
    See [https://python-jsonschema.readthedocs.io/en/latest/errors/]
    for details about the information it carries.
    """

    def __init__(self, source:ValidationError = None):
        self.source = source

    def __getattr__(self, attr):
        return getattr(self.source, attr)