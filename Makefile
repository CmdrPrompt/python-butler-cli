include .butler/Makefile

# ---------------------------------------------------------------------------
# Local targets
# ---------------------------------------------------------------------------

.PHONY: activate _help-local

# Hook into butler's help target by adding a prerequisite
help: _help-local

_help-local:
	@echo "  Activate virtual environment:"
	@echo "    make activate            -- Print how to activate .venv"
	@echo "    eval \$$(make -s activate) -- Activate in the current shell"
	@echo ""

activate:
	@echo ""
	@echo "To activate the virtual environment, run:"
	@echo ""
	@echo "    source .venv/bin/activate"
	@echo ""
	@echo "To activate without a separate step, run:"
	@echo ""
	@echo "    eval \$$(make -s activate)"
	@echo ""
