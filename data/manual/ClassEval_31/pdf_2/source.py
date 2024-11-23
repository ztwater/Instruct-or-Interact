class DataStatistics4:
    def pdf(data, mean, std_dev):
        pdf_values = norm.pdf(data, mean, std_dev)
        return pdf_values