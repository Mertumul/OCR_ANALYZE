from modules.type_detector import extract_patterns
from validator.cc_validate import is_cc_valid
from validator.domain_validate import check_dns_lookup
from validator.email_validate import (fetch_email_verification,
                                       is_email_deliverable)
from validator.tc_validate import tc_validate
from validator.url_validate import is_url_valid
import dateparser


async def analyze_text(input_text: str) -> dict:
    """
    Analyses the input text for various patterns and extracts findings.

    Args:
        input_text (str): The input text to be analyzed.

    Returns:
        dict: Analysis results containing content, status, and findings.
    """
    findings = []

    # Extract patterns
    extracted_data = await extract_patterns(input_text)

    # Convert extracted data to findings
    for pattern_name, matches in extracted_data.items():
        for match in matches:
            match_result = await match_case(pattern_name, match)

            if match_result.get("type") == "DATE":
                parsed_date = dateparser.parse(match_result.get("value"))
                if parsed_date:
                    formatted_date = parsed_date.strftime("%Y-%m-%d %H:%M:%S")
                    match_result["value"] = formatted_date  # Bu satır ile "value" anahtarını güncelledik

            findings.append(match_result)

    result = {"content": input_text, "status": "successful", "findings": findings}
    return result


async def match_case(pattern_name: str, match: str) -> dict:
    """
    Matches a sensitive data pattern case and performs further validation if needed.

    Args:
        pattern_name (str): The name of the sensitive data pattern.
        match (str): The matching data value.

    Returns:
        dict: Match result including value, type, and additional validation details.
    """
    match_result = {"value": match, "type": pattern_name}

    match_result |= await match_credit_card_number(pattern_name, match)
    match_result |= await match_email(pattern_name, match)
    match_result |= await match_domain(pattern_name, match)
    match_result |= await match_url(pattern_name, match)
    match_result |= await match_id_number(pattern_name, match)

    return match_result


async def match_credit_card_number(pattern_name, match):
    if pattern_name == "CREDIT_CARD_NUMBER":
        card_valid = await is_cc_valid(match)
        return {"valid": card_valid}
    return {}


async def match_id_number(pattern_name, match):
    if pattern_name == "ID_NUMBER":
        id_valid = await tc_validate(match)
        return {"valid": id_valid}
    return {}


async def match_email(pattern_name, match):
    if pattern_name == "EMAIL":
        email_result = await fetch_email_verification(match)
        if email_result:
            email_deliverable = await is_email_deliverable(email_result)
            return {"valid": email_deliverable}
        else:
            return {"valid": False}
    return {}


async def match_domain(pattern_name, match):
    if pattern_name == "DOMAIN":
        domain_valid = await check_dns_lookup(match)
        return {"valid": domain_valid}
    return {}


async def match_url(pattern_name, match):
    if pattern_name == "URL":
        url_valid = await is_url_valid(match)
        return {"valid": url_valid}
    return {}
