#!/usr/bin/env python3
"""
Test script to verify the agent implementation structure
This tests the code structure without making actual API calls
"""

import sys
import os

# Add agents directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'agents'))

def test_imports():
    """Test that all modules can be imported"""
    print("Testing imports...")
    
    try:
        # Test jenny module import
        import jenny
        print("✓ jenny module imported successfully")
        
        # Test jenny_api module import
        import jenny_api
        print("✓ jenny_api module imported successfully")
        
        # Check that JennyAgent class exists
        assert hasattr(jenny, 'JennyAgent'), "JennyAgent class not found"
        print("✓ JennyAgent class exists")
        
        # Check that FastAPI app exists
        assert hasattr(jenny_api, 'app'), "FastAPI app not found"
        print("✓ FastAPI app exists")
        
        # Check endpoints
        routes = [route.path for route in jenny_api.app.routes]
        assert '/' in routes, "Root endpoint not found"
        assert '/health' in routes, "Health endpoint not found"
        assert '/jenny' in routes, "Jenny endpoint not found"
        print("✓ All required endpoints exist")
        
        return True
        
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False
    except AssertionError as e:
        print(f"✗ Assertion error: {e}")
        return False
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return False


def test_file_structure():
    """Test that all expected files exist"""
    print("\nTesting file structure...")
    
    expected_files = [
        'README.md',
        'START_HERE.md',
        'requirements.txt',
        '.env.example',
        'agents/jenny.py',
        'agents/jenny_api.py',
        'agents/README.md',
        'agents/example_usage.py',
        'agents/example_api_client.py',
        'docs/Learn.md',
        'docs/Teach.md',
        'docs/Master.md',
    ]
    
    all_exist = True
    for file in expected_files:
        if os.path.exists(file):
            print(f"✓ {file} exists")
        else:
            print(f"✗ {file} missing")
            all_exist = False
    
    return all_exist


def test_requirements():
    """Test that requirements.txt has necessary packages"""
    print("\nTesting requirements.txt...")
    
    with open('requirements.txt', 'r') as f:
        content = f.read()
    
    required_packages = ['openai', 'python-dotenv', 'fastapi', 'uvicorn']
    all_present = True
    
    for package in required_packages:
        if package in content:
            print(f"✓ {package} in requirements.txt")
        else:
            print(f"✗ {package} missing from requirements.txt")
            all_present = False
    
    return all_present


def main():
    """Run all tests"""
    print("=" * 60)
    print("Python Agent Implementation Tests")
    print("=" * 60)
    
    results = []
    
    # Test file structure
    results.append(test_file_structure())
    
    # Test requirements
    results.append(test_requirements())
    
    # Test imports
    results.append(test_imports())
    
    # Summary
    print("\n" + "=" * 60)
    if all(results):
        print("✅ ALL TESTS PASSED!")
        print("=" * 60)
        return 0
    else:
        print("❌ SOME TESTS FAILED")
        print("=" * 60)
        return 1


if __name__ == "__main__":
    sys.exit(main())
