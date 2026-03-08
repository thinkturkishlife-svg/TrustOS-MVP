-- SQLite schema for TrustOS MVP trustee data.

CREATE TABLE IF NOT EXISTS trustees (
    id INTEGER PRIMARY KEY,
    trustee_name TEXT,
    minimum_assets INTEGER,
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
    fee_structure,
    jurisdiction,
    directed_trust_supported,
    external_advisor_supported,
    custodian_platform,
    asset_types_supported
) VALUES
    (1, 'Wealth Advisors Trust Company', 1000000, 'AUM-based annual fee', 'South Dakota', 1, 1, 'Schwab', 'Marketable securities, cash, alternatives'),
    (2, 'Sterling Trustees', 500000, 'Tiered annual fee', 'Nevada', 1, 1, 'Fidelity', 'Marketable securities, cash'),
    (3, 'National Advisors Trust', 250000, 'Flat + AUM hybrid fee', 'Kansas', 1, 1, 'Multi-custodian', 'Marketable securities, cash, private assets'),
    (4, 'Members Trust Company', 1000000, 'AUM-based annual fee', 'New Hampshire', 1, 1, 'Pershing', 'Marketable securities, cash, concentrated stock'),
    (5, 'Peak Trust', 2000000, 'Custom negotiated fee', 'Alaska', 1, 1, 'Schwab', 'Marketable securities, cash, real estate, alternatives'),
    (6, 'Arden Trust', 750000, 'AUM-based annual fee', 'South Dakota', 1, 1, 'Schwab', 'Marketable securities, cash, private funds'),
    (7, 'South Dakota Trust Company', 500000, 'Tiered annual fee', 'South Dakota', 1, 0, 'Multi-custodian', 'Marketable securities, cash, closely held business interests'),
    (8, 'Bridgeford Trust', 1000000, 'Flat annual trustee fee', 'South Dakota', 1, 1, 'Fidelity', 'Marketable securities, cash, alternatives'),
    (9, 'Cumberland Trust', 2500000, 'AUM + administration fee', 'Tennessee', 0, 1, 'Multi-custodian', 'Marketable securities, cash, family business holdings'),
    (10, 'Prairie Trust', 300000, 'Tiered annual fee', 'South Dakota', 1, 1, 'Schwab', 'Marketable securities, cash'),
    (11, 'Premier Trust', 500000, 'AUM-based annual fee', 'Nevada', 1, 1, 'Fidelity', 'Marketable securities, cash, alternatives');
