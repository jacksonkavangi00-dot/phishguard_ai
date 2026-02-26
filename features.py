from urllib.parse import urlparse
import re

def extract_features(url):
    features = []
    parsed = urlparse(url)

    # URL length
    features.append(len(url))

    # Domain length
    features.append(len(parsed.netloc))

    # Count dots
    features.append(url.count('.'))

    # Count hyphens
    features.append(url.count('-'))

    # Count @ symbol
    features.append(url.count('@'))

    # Count query parameters
    features.append(url.count('?'))

    # HTTPS present
    features.append(1 if parsed.scheme == "https" else 0)

    # IP address in URL
    features.append(1 if re.search(r"\d+\.\d+\.\d+\.\d+", url) else 0)

    # Suspicious words
    suspicious_words = ['login','secure','bank','verify','update','paypal','mpesa']
    features.append(sum(word in url.lower() for word in suspicious_words))

    return features
