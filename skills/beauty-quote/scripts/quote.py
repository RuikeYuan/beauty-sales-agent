"""Exact arithmetic for the fictional training store, rule version v1."""
import argparse
import json


def calculate(visits: int, used: int) -> dict:
    if type(visits) is not int or visits < 0:
        raise ValueError("visits must be a non-negative integer")
    if type(used) is not int or not 0 <= used <= 4:
        raise ValueError("used must be an integer from 0 through 4")
    cards, singles = divmod(visits, 4)
    return {
        "rule_version": "fictional-v1",
        "currency": "CNY",
        "planned_visits": visits,
        "all_single_total": visits * 240,
        "combination": {"cards": cards, "singles": singles,
                        "total": cards * 880 + singles * 240},
        "one_card": {"upfront": 880, "validity_months": 4,
                     "used_visits": used, "consumed": used * 220,
                     "unused_visits": 4 - used,
                     "refundable_unused": (4 - used) * 220,
                     "net_after_refund": used * 220,
                     "same_visits_as_singles": used * 240,
                     "saving_after_refund": used * 20},
        "excludes": ["first_visit_trial", "extras"],
        "assumptions": ["unchanged_prices", "valid_order_refund_terms",
                        "card_validity_requires_separate_review"],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--visits", type=int, required=True)
    parser.add_argument("--used", type=int, default=0)
    args = parser.parse_args()
    try:
        result = calculate(args.visits, args.used)
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
