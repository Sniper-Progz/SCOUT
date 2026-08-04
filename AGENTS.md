# SCOUT Operating Agreement

## Mission

SCOUT is an autonomous market intelligence platform. Its job is to observe markets, collect and normalize intelligence, score opportunities, analyze news, build historical datasets, generate recommendations, and mirror completed trade snapshots from IVY after execution. SCOUT does not execute trades, place orders, manage risk, or manage positions.

SCOUT must remain useful if IVY does not exist.

## Project Goals

- Maintain strict modular boundaries.
- Keep every capability broker-neutral at the higher layers.
- Make all behavior deterministic unless external data sources are being observed.
- Build only framework, interfaces, tests, and documentation until a feature is explicitly requested.
- Keep the repository independent from IVY source code and implementation details.

## Architecture Philosophy

- Prefer small, explicit interfaces over implicit coupling.
- Inject dependencies instead of creating them globally.
- Keep domain contracts in shared, broker-neutral models.
- Keep provider adapters behind interfaces.
- Avoid circular imports by making dependencies flow inward toward shared contracts and interfaces.
- Treat configuration, orchestration, data collection, analysis, and reporting as separate concerns.

## Module Boundaries

- `runtime`: process orchestration and lifecycle coordination only.
- `configuration`: environment and settings access only.
- `logging`: structured logging and log formatting only.
- `health_monitoring`: health snapshots and checks only.
- `scanner`: candidate discovery and opportunity scoring entry points only.
- `market_data`: market data abstractions and provider adapters only.
- `news`: news intake, normalization, and feed abstractions only.
- `catalyst_analysis`: event and catalyst evaluation only.
- `finbert`: sentiment inference boundary only.
- `rss`: RSS ingestion boundary only.
- `sec`: SEC filing ingestion boundary only.
- `analytics`: derived metrics and historical analysis only.
- `replay`: completed-trade replay and mirror preparation only.
- `synchronization`: versioned communication prep only; do not implement IVY communication yet.
- `historical_database`: historical storage abstractions only.
- `reporting`: recommendation and intelligence output only.
- `utilities`: small pure helpers only.
- `interfaces`: protocol definitions and service contracts only.
- `shared_contracts`: broker-neutral data models only.

## Coding Standards

- Use Python 3.12+.
- Require strict typing everywhere.
- Use type annotations for every public function, method, and module-level constant.
- Prefer dataclasses with `slots=True` and `frozen=True` for immutable contracts.
- Avoid hidden side effects.
- Keep public APIs narrow and explicit.
- Use ASCII unless a file already requires a different character set.

## Testing Standards

- Use `pytest`.
- Add tests for every new interface, contract, and module boundary.
- Verify package layout and importability.
- Keep tests deterministic and isolated from live market data.
- Mock external providers at the interface boundary.
- Every completed feature must pass `ruff`, `mypy`, and `pytest` before commit.

## Commit Policy

- Commit in small, atomic steps.
- Never leave the working tree dirty at the end of a finished task.
- Commit messages should describe one logical change.
- Push each completed feature to GitHub after the related commit is validated.
- Do not amend commits unless explicitly requested.

## Documentation Standards

- Keep repository documentation current with architecture changes.
- Document module responsibilities before adding implementation.
- Preserve this file as the governing document for SCOUT development.
- Add docstrings to packages, contracts, and protocols that future contributors will need to understand quickly.

## Dependency Rules

- Do not import from IVY.
- Do not copy IVY source code.
- Do not create hidden runtime dependencies on IVY.
- Keep higher-level modules dependent only on interfaces and shared contracts.
- Keep provider-specific code isolated in adapter modules.

## Versioning Rules

- Use semantic versioning for the Python package.
- Treat shared contracts as versioned interfaces.
- Any future IVY communication protocol must be explicitly versioned and backwards compatibility must be considered before adoption.
- Add breaking changes only with a version bump and migration notes.

## Security Policy

- Never store secrets in the repository.
- Read credentials from the environment or injected configuration sources only.
- Avoid logging sensitive payloads.
- Treat external feeds, news, and filings as untrusted input.
- Sanitize and normalize all incoming text before it reaches shared contracts.

## Performance Requirements

- Keep default behavior lightweight.
- Prefer streaming and bounded collection patterns over unbounded accumulation.
- Avoid unnecessary copies of large market datasets.
- Make performance characteristics obvious in docstrings when an interface may process large volumes.

## Determinism Requirements

- Deterministic behavior is required for tests and for any logic that can be made pure.
- Sort or stabilize outputs before returning them when the source order is not guaranteed.
- Keep timestamps and randomness injected through interfaces.
- Never depend on ambient global state.

## GitHub Workflow

- Develop locally in the SCOUT repository only.
- Keep the remote repository independent from IVY.
- Push validated commits to `Sniper-Progz/SCOUT`.
- Use pull requests for substantial future changes if the workflow expands beyond direct pushes.

## Definition of Done

- The feature is fully typed.
- The feature has tests.
- `ruff` passes.
- `mypy` passes.
- `pytest` passes.
- Documentation is updated.
- The working tree is clean.
- The change is committed and pushed.

## Future Roadmap

1. Add provider adapters behind the market data abstraction.
2. Add historical storage interfaces and a concrete persistence layer.
3. Add deterministic scanner and scoring pipelines.
4. Add news ingestion and catalyst analysis adapters.
5. Add replay support for completed trade snapshots.
6. Define the versioned SCOUT-to-IVY communication contract.
7. Expand reporting and downstream advisory outputs.

