import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri

pandas2ri.activate()
biocmanager = importr('BiocManager')
biocmanager.install('TCGAbiolinks')
tcgabiolinks = importr('TCGAbiolinks')

# R code as a string
r_code = """
library(TCGAbiolinks)

query <- GDCquery(
  project = "TCGA-BRCA",
  data.category = "Transcriptome Profiling",
  data.type = "Gene Expression Quantification",
  workflow.type = "HTSeq - FPKM"
)
GDCdownload(query)
data <- GDCprepare(query)

data
"""

# Execute the R code
r_data = robjects.r(r_code)

# Convert R dataframe to pandas dataframe
import pandas as pd

data_df = pandas2ri.ri2py(r_data)
data_df.to_csv("tcga_brca_data.csv")
