import great_expectations as ge
import pandas as pd
from great_expectations.core.batch import RuntimeBatchRequest

# Create a Pandas DataFrame
df = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})

# Instantiate a DataContext
context = ge.DataContext

context = ge.get_context()


datasource_config = {
    "name": "example_datasource",
    "class_name": "Datasource",
    "module_name": "great_expectations.datasource",
    "execution_engine": {
        "module_name": "great_expectations.execution_engine",
        "class_name": "PandasExecutionEngine",
    },
    "data_connectors": {
        "default_runtime_data_connector_name": {
            "class_name": "RuntimeDataConnector",
            "module_name": "great_expectations.datasource.data_connector",
            "batch_identifiers": ["default_identifier_name"],
        },
    },
}

context.add_datasource(**datasource_config)

df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=["a", "b", "c"])


batch_request = RuntimeBatchRequest(
    datasource_name="version-0.15.50 example_datasource",
    data_connector_name="version-0.15.50 default_runtime_data_connector_name",
    data_asset_name="version-0.15.50 <your_meaningful_name>",  # This can be anything that identifies this data_asset for you
    runtime_parameters={"batch_data": df},  # df is your dataframe
    batch_identifiers={"default_identifier_name": "default_identifier"},
)


context.add_or_update_expectation_suite(
    expectation_suite_name="version-0.15.50 test_suite"
)
validator = context.get_validator(
    batch_request=batch_request, expectation_suite_name="version-0.15.50 test_suite"
)
print(validator.head())

# Add a Datasource
context.add_datasource(
    "my_datasource",
    class_name="PandasDatasource",
    batch_kwargs_generators={
        "my_generator": {
            "class_name": "PandasBatchKwargsGenerator",
            "assets": {"df": df},
        }
    },
)

# Create an ExpectationSuite
suite = context.create_expectation_suite("my_suite")

# Connect the DataFrame to the DataContext
batch = context.get_batch({"df": df}, "my_datasource")

# Add an expectation to the suite
suite.expect_column_values_to_be_between("col1", 1, 3)

# Validate the batch against the expectation
results = context.run_validation_operator("my_suite", assets_to_validate=[batch])
