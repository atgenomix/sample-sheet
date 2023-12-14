Quick Start
===========

To demonstrate the features of this library we will use a test file at an HTTPS endpoint.
To follow along, ensure you have the `smart_open` library installed!

.. code-block:: python

   >>> from sample_sheet import SampleSheetV2
   >>> url = 'https://raw.githubusercontent.com/atgenomix/sample-sheet-V2/v2-support/tests/resources/V2-paired-end.csv'
   >>> sample_sheet = SampleSheetV2(url)


The metadata of the sample sheet can be accessed with the ``Header``,
``Reads`` and, ``BCLConvert_Settings`` attributes:

.. code-block:: python

   >>> sample_sheet.Header
   {'FileFormatVersion': '2', 'RunName': 'NextSeq2K20231109', 'InstrumentPlatform': 'NextSeq1k2k', 'IndexOrientation': 'Forward'}
   >>> sample_sheet.Reads
   {'Read1Cycles': '151', 'Read2Cycles': '151', 'Index1Cycles': '8', 'Index2Cycles': '10'}
   >>> sample_sheet.is_paired_end
   True
   >>> sample_sheet.BCLConvert_Settings
   {'SoftwareVersion': '3.10.12', 'OverrideCycles': 'Y151;I8;U10;Y151', 'BarcodeMismatchesIndex1': '1', 'FastqCompressionFormat': 'gzip'}

The samples can be accessed directly or *via* iteration:

.. code-block:: python

   >>> sample_sheet.samples
   [Sample({'Sample_ID': '1823A', 'Sample_Name': None, 'index': 'GTCTGTCA'}), Sample({'Sample_ID': '1823B', 'Sample_Name': None, 'index': 'TGAAGAGA'}), Sample({'Sample_ID': '1823C', 'Sample_Name': None, 'index': 'TTCACGCA'})]
   >>> first_sample, *other_samples = list(sample_sheet)
   >>> first_sample
   Sample({'Sample_ID': '1823A', 'Sample_Name': None, 'index': 'GTCTGTCA'})

Defining Sample Read Structures
-------------------------------

If a column labeled ``Read_Structure`` is provided *per* sample, then
additional functionality is enabled.

.. code-block:: python

   >>> first_sample, *_ = sample_sheet.samples
   >>> first_sample.Read_Structure

