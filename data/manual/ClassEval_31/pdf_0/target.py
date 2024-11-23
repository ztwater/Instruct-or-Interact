class DataStatistics4:
    def pdf(data, mu, sigma):
        pdf_values = norm.pdf(data, mu, sigma)
        return pdf_values