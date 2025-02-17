"""Completeness

Verify that the recipe is not missing anything essential.
"""

import os

import conda_build.license_family

# from . import ERROR, INFO
from . import WARNING, LintCheck


class missing_build_number(LintCheck):
    """The recipe is missing a build number

    Please add::

        build:
            number: 0
    """

    def check_recipe(self, recipe):
        if not recipe.get("build/number", ""):
            self.message(section="build")


class missing_home(LintCheck):
    """The recipe is missing a homepage URL

    Please add::

       about:
          home: <URL to homepage>

    """

    def check_recipe(self, recipe):
        if not recipe.get("about/home", ""):
            self.message(section="about")


class missing_summary(LintCheck):
    """The recipe is missing a summary

    Please add::

       about:
         summary: One line briefly describing package

    """

    def check_recipe(self, recipe):
        if not recipe.get("about/summary", ""):
            self.message(section="about")


class missing_license(LintCheck):
    """The recipe is missing the ``about/license`` key.

    Please add::

        about:
           license: <name of license>

    """

    def check_recipe(self, recipe):
        if not recipe.get("about/license", ""):
            self.message(section="about")


class missing_license_file(LintCheck):
    """The recipe is missing the ``about/license_file`` key.

    Please add::

        about:
           license_file: <license file name>

    or::

        about:
           license_file:
                - <license file name>
                - <license file name>

    """

    def check_recipe(self, recipe):
        if not recipe.get("about/license_file", ""):
            self.message(section="about")


class missing_license_family(LintCheck):
    """The recipe is missing the ``about/license_family`` key.

    Please add::

        about:
           license_family: <license_family>

    """

    def check_recipe(self, recipe):
        if not recipe.get("about/license_family", ""):
            self.message(section="about")


class invalid_license_family(LintCheck):
    """The recipe has an incorrect ``about/license_family`` value.

    Please change::

        about:
           license_family: <license_family>

    """

    def check_recipe(self, recipe):
        license_family = recipe.get("about/license_family", "")
        if license_family and not license_family.lower() in [
            x.lower() for x in conda_build.license_family.allowed_license_families
        ]:
            self.message(section="about")


class missing_tests(LintCheck):
    """The recipe is missing tests.

    Please add::

        test:
            commands:
               - some_command

    and/or::

        test:
            imports:
               - some_module


    and/or any file named ``run_test.py`, ``run_test.sh`` or
    ``run_test.pl`` executing tests.

    """

    test_files = ["run_test.py", "run_test.sh", "run_test.pl"]

    def check_recipe(self, recipe):
        if any(os.path.exists(os.path.join(recipe.dir, f)) for f in self.test_files):
            return
        if recipe.get("test/commands", "") or recipe.get("test/imports", ""):
            return
        if recipe.get("test", False) is not False:
            self.message(section="test")
        else:
            self.message()


class missing_hash(LintCheck):
    """The recipe is missing a sha256 checksum for a source file

    Please add::

       source:
         sha256: checksum-value

    Note: md5 and sha1 are deprecated.

    """

    checksum_names = ["sha256"]

    def check_source(self, source, section):
        if not any(source.get(chk) for chk in self.checksum_names):
            self.message(section=section)


class missing_source(LintCheck):
    """The recipe is missing a URL for the source

    Please add::

        source:
            url: <URL to source>

    Or::
        source:
            - url: <URL to source>

    """

    source_types = ["url", "git_url", "hg_url", "svn_url"]

    def check_source(self, source, section):
        if not any(source.get(chk) for chk in self.source_types):
            self.message(section=section)


class non_url_source(LintCheck):
    """A source of the recipe is not url of url type.

    Please change to::

        source:
            url: <URL to source>

    """

    source_types = ["git_url", "hg_url", "svn_url"]

    def check_source(self, source, section):
        if any(source.get(chk) for chk in self.source_types):
            self.message(section=section, severity=WARNING)


class missing_doc_url(LintCheck):
    """The recipe is missing a doc_url

    Please add::

        about:
            doc_url: some_documentation_url

    """

    def check_recipe(self, recipe):
        if not recipe.get("about/doc_url", ""):
            self.message(section="about")


class missing_doc_source_url(LintCheck):
    """The recipe is missing a doc_source_url

    Please add::

        about:
            doc_source_url: some-documentation-source-url

    """

    def check_recipe(self, recipe):
        if not recipe.get("about/doc_source_url", ""):
            self.message(section="about", severity=WARNING)


class missing_dev_url(LintCheck):
    """The recipe is missing a dev_url

    Please add::

        about:
            dev_url: some-dev-url

    """

    def check_recipe(self, recipe):
        if not recipe.get("about/dev_url", ""):
            self.message(section="about")


class missing_license_url(LintCheck):
    """The recipe is missing a license_url

    Please add::

        about:
            dev_url: some-dev-url

    """

    def check_recipe(self, recipe):
        if not recipe.get("about/license_url", ""):
            self.message(section="about", severity=WARNING)


class missing_description(LintCheck):
    """The recipe is missing a description

    Please add::

        about:
            description: some-description

    """

    def check_recipe(self, recipe):
        if not recipe.get("about/description", ""):
            self.message(section="about", severity=WARNING)
