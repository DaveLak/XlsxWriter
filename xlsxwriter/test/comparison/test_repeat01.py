###############################################################################
#
# Tests for XlsxWriter.
#
# SPDX-License-Identifier: BSD-2-Clause
# Copyright (c), 2013-2024, John McNamara, jmcnamara@cpan.org
#

from ...workbook import Workbook
from ..excel_comparison_test import ExcelComparisonTest


class TestCompareXLSXFiles(ExcelComparisonTest):
    """
    Test file created by XlsxWriter against a file created by Excel.

    """

    def setUp(self):
        self.set_filename("repeat01.xlsx")

        self.ignore_files = [
            "xl/printerSettings/printerSettings1.bin",
            "xl/worksheets/_rels/sheet1.xml.rels",
        ]
        self.ignore_elements = {
            "[Content_Types].xml": ['<Default Extension="bin"'],
            "xl/worksheets/sheet1.xml": ["<pageMargins", "<pageSetup"],
        }

    def test_create_file(self):
        """Test the creation of a simple XlsxWriter file with repeat rows."""

        workbook = Workbook(self.got_filename)

        worksheet = workbook.add_worksheet()

        worksheet.repeat_rows(0)

        worksheet.write("A1", "Foo")

        workbook.close()

        self.assertExcelEqual()
