-- SQLite schema for TrustOS MVP trustee data.

CREATE TABLE IF NOT EXISTS trustees (
    id INTEGER PRIMARY KEY,
    trustee_name TEXT,
    minimum_assets INTEGER,
    fee_bps INTEGER,
    fee_structure TEXT,
    jurisdiction TEXT,
    directed_trust_supported BOOLEAN,
    external_advisor_supported BOOLEAN,
    custodian_platform TEXT,
    asset_types_supported TEXT
);

INSERT INTO trustees (
    id,
    trustee_name,
    minimum_assets,
    fee_bps,
    fee_structure,
    jurisdiction,
    directed_trust_supported,
    external_advisor_supported,
    custodian_platform,
    asset_types_supported
) VALUES
    (1, 'Wealth Advisors Trust Company', 1000000, 50, 'AUM-based annual fee (0.45%-0.85%)', 'South Dakota', 1, 1, 'Schwab', 'Marketable securities, cash, alternatives, private funds'),
    (2, 'Sterling Trustees', 500000, 35, 'Tiered annual fee + account admin surcharge', 'Nevada', 1, 1, 'Fidelity', 'Marketable securities, cash, concentrated stock'),
    (3, 'Arden Trust', 750000, 55, 'AUM-based annual fee (breakpoint schedule)', 'South Dakota', 1, 1, 'Schwab', 'Marketable securities, cash, private equity, real estate LLCs'),
    (4, 'Bridgeford Trust', 1000000, 60, 'Flat trustee fee + specialty asset add-ons', 'South Dakota', 1, 1, 'Fidelity', 'Marketable securities, cash, alternatives, private notes'),
    (5, 'South Dakota Trust Company', 500000, 70, 'Tiered annual fee with minimum annual billing', 'South Dakota', 1, 0, 'Multi-custodian', 'Marketable securities, cash, closely held business interests'),
    (6, 'National Advisors Trust', 250000, 60, 'Flat + AUM hybrid fee', 'Kansas', 1, 1, 'Multi-custodian', 'Marketable securities, cash, private assets, alternatives');
    
